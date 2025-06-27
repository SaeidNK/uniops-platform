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

## 📸 Screenshots (Optional)

Add:  
- Diagram of architecture  
- Terminal output of `terraform apply` and `ansible-playbook`  
- Grafana dashboard (Phase 4)  

---

## 🧠 Why This Project?

This project was built to demonstrate:  
- End-to-end cloud automation  
- DevOps best practices  
- Scalable infrastructure deployment  
- Monitoring and visibility for real-world systems
