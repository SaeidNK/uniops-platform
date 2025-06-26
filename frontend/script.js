function sendQuery() {
  const query = document.getElementById("query").value;

  fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: query })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("response").innerText = data.response || JSON.stringify(data, null, 2);
  })
  .catch(err => {
    document.getElementById("response").innerText = "Error: " + err;
  });
}
