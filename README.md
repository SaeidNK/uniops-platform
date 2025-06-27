# UniOps Platform 🚀  
**Smart Infrastructure Monitoring and Support Platform**

UniOps is a cloud-based infrastructure project designed to showcase hands-on skills in provisioning, automation, and monitoring using industry-standard tools like **Terraform**, **Ansible**, **AWS EC2**, and **Node Exporter**. Built for real-world DevOps workflows, the platform supports scalable infrastructure setup and system-level monitoring.

---

## 🛠️ Technologies Used

| Layer              | Tools & Tech                     |
|--------------------|----------------------------------|
| Infrastructure     | Terraform (AWS EC2)              |
| Configuration Mgmt | Ansible                          |
| Monitoring         | Prometheus Node Exporter         |
| Web Server         | Nginx (simulated traffic)        |
| Automation Shell   | GitHub + Ansible Playbooks       |
| OS & Platform      | Ubuntu 22.04 on EC2 via WSL      |

---

## 📦 Project Structure

uniops-platform/
├── infra/                 # Terraform files
├── ansible/               # Ansible playbooks and inventory
├── backend/               # Flask-based Chatbot backend
│   ├── app.py             # Chatbot logic and endpoints
│   └── requirements.txt   # Python dependencies
├── frontend/              # HTML/JS Chatbot UI
│   ├── index.html
│   └── script.js
├── .github/workflows/     # GitHub Actions CI
├── .gitignore
├── README.md

---

## ⚙️ Phase Overview

- ✅ **Phase 1**: GitHub Repo Setup  
- ✅ **Phase 2**: EC2 Provisioning with Terraform  
- ✅ **Phase 3**: Ansible Setup (Python, Nginx, Node Exporter)  
- 🔜 **Phase 4**: Prometheus & Grafana Monitoring Dashboards  
- 🔄 **Phase 5**: Support Automation (Chatbot, Alerting, CI/CD)  

---

## 🌐 Live Monitoring Example

> Metrics exposed at:  
> `http://<ec2-public-ip>:9100/metrics`  
(Replace with your EC2 IP — optional link)

---

## 📸 Screenshots 
![Grafana Screenshot](screenshot/Grafana.png)
![Chatbot Screenshot](screenshot/frontend.png
![Ansible Screenshot](screenshot/Ansibe.png)
![Terraform1 Screenshot](screenshot/Terraform1.png)
![Terraform2 Screenshot](screenshot/Terraform2.png)

---
## 🚀 How to Use This Project
This guide explains how to deploy and run the UniOps Platform — a cloud-based monitoring and support solution using EC2, Terraform, Ansible, Prometheus, Grafana, and a Flask-based chatbot.

# ✅ Prerequisites
AWS account with IAM user and access key

SSH PEM key (e.g., keyPair.pem) for EC2 login

Tools installed locally:

Terraform

Ansible

AWS CLI

Git

# 🧱 Project Setup Steps
# 1. Clone the Repository
bash
Copy code
git clone https://github.com/SaeidNK/uniops-platform.git
cd uniops-platform
# 2. Configure AWS Credentials
bash
Copy code
aws configure
Enter:

AWS Access Key ID

AWS Secret Access Key

Region (e.g., eu-west-2)

Output format (e.g., json)

# 3. Provision EC2 Instance (Terraform)
bash
Copy code
cd infra
terraform init
terraform apply
✅ This launches an Ubuntu EC2 instance and outputs the public IP address.

# 4. Configure and Provision the Server (Ansible)
Move your PEM key:

bash
Copy code
mkdir -p ~/.ssh
cp path/to/keyPair.pem ~/.ssh/uniops-key.pem
chmod 400 ~/.ssh/uniops-key.pem
Create/edit the inventory:

ini
Copy code
[uniops]
<your-ec2-ip> ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/uniops-key.pem
Run the playbook:

bash
Copy code
cd ../ansible
ansible-playbook -i inventory.ini playbook.yml
This installs:

Nginx (for simulated load)

Node Exporter

Prometheus

Grafana

Flask & Python packages

# 5. Start the Chatbot Flask Service
SSH into your EC2 instance:

bash
Copy code
ssh -i ~/.ssh/uniops-key.pem ubuntu@<your-ec2-ip>
Run:

bash
Copy code
cd ~/uniops_chatbot/backend
sudo systemctl start uniops-chatbot
sudo systemctl enable uniops-chatbot
Verify:

bash
Copy code
curl http://localhost:5000/cpu
# 🌐 Access the Platform
Component	URL Example
# Web Chat UI	http://<your-ec2-ip>
# Chatbot API	http://<your-ec2-ip>:5000/ask
# Prometheus	http://<your-ec2-ip>:9090
# Node Exporter	http://<your-ec2-ip>:9100/metrics
# Grafana	http://<your-ec2-ip>:3000 (default login: admin / admin)

⚠️ Make sure ports 22, 80, 3000, 5000, 9090, and 9100 are open in your EC2 Security Group.

# 🧪 Example Usage
Query the chatbot via curl:

bash
Copy code
curl -X POST http://<your-ec2-ip>:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"query":"/cpu"}'
Or use the frontend UI to enter /cpu, /disk, /memory, etc.
