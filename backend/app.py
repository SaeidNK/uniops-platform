from flask import Flask, request, jsonify
import requests
import logging
import psutil
from flask import Flask, request, jsonify

# Logging setup
logging.basicConfig(
    filename="uniops_chatbot.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


app = Flask(__name__)
PROMETHEUS = "http://localhost:9090"

@app.route("/")
def index():
    return "UniOps Chatbot is running!"
@app.route("/cpu")
def cpu_usage():
    return {"cpu_percent": psutil.cpu_percent(interval=1)}
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "").lower()

    logging.info(f"Received query: {query}")

    if "/cpu" in query:
        return jsonify(cpu_usage())
    elif "/disk" in query:
        return jsonify(disk_status())
    elif "/memory" in query:
        return jsonify(memory_status())
    elif "/uptime" in query:
        return jsonify(uptime_status())
    elif "/help" in query:
        return jsonify({
            "response": "Commands: /cpu, /disk, /memory, /uptime, /help"
        })
    else:
        return jsonify({
            "response": "Unknown command. Type /help."
        })

def cpu_usage():
    url = f"{PROMETHEUS}/api/v1/query?query=100-(avg by(instance)(irate(node_cpu_seconds_total{{mode='idle'}}[1m])) * 100)"
    try:
        r = requests.get(url).json()
        value = float(r["data"]["result"][0]["value"][1])
        return {"response": f"Current CPU usage is {value:.2f}%"}
    except:
        logging.exception("An error occurred while processing query")
        return {"response": "CPU data not available."}

def disk_status():
    url = f"{PROMETHEUS}/api/v1/query?query=node_filesystem_avail_bytes"
    try:
        r = requests.get(url).json()
        result = r["data"]["result"]
        if not result:
            return {"response": "Disk data not available."}
        response = []
        for item in result[:3]:  # Limit output
            fs = item["metric"].get("mountpoint", "/")
            val = float(item["value"][1]) / 1e9
            response.append(f"{fs}: {val:.2f} GB free")
        return {"response": "\n".join(response)}
    except:
        logging.exception("An error occurred while processing query")
        return {"response": "Disk data fetch error."}

def memory_status():
    try:
        used_url = f"{PROMETHEUS}/api/v1/query?query=node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes"
        total_url = f"{PROMETHEUS}/api/v1/query?query=node_memory_MemTotal_bytes"

        used = float(requests.get(used_url).json()["data"]["result"][0]["value"][1])
        total = float(requests.get(total_url).json()["data"]["result"][0]["value"][1])
        percent = (used / total) * 100
        return {"response": f"Memory usage: {percent:.2f}% ({used/1e9:.2f}GB used of {total/1e9:.2f}GB)"}
    except:
       logging.exception("An error occurred while processing query")
       return {"response": "Memory data fetch error."}

def uptime_status():
    try:
        url = f"{PROMETHEUS}/api/v1/query?query=node_time_seconds - node_boot_time_seconds"
        r = requests.get(url).json()
        seconds = float(r["data"]["result"][0]["value"][1])
        hours = seconds / 3600
        return {"response": f"System uptime: {hours:.1f} hours"}
    except:
        logging.exception("An error occurred while processing query")
        return {"response": "Uptime data not available."}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
