# 🛡️ Security Log Analyzer Dashboard

A Python-based cybersecurity dashboard that analyzes authentication logs, identifies suspicious activity, and detects possible brute-force attacks.

## 📌 Project Overview

The Security Log Analyzer processes login event data and presents security information through an interactive Streamlit dashboard.

It helps identify:

- Failed login attempts
- Successful logins
- Suspicious IP addresses
- Repeated authentication failures
- Possible brute-force attacks
- Login activity by time

## 🚀 Features

- Upload and analyze CSV security logs
- Automatic summary statistics
- Brute-force attack detection
- Suspicious IP detection
- Severity classification
- Failed-login visualization
- Security event timeline
- Raw log filtering
- Interactive Streamlit dashboard

## 🛠 Technologies Used

- Python
- Pandas
- Streamlit
- Data Analysis
- Cybersecurity Monitoring
- Git
- GitHub

## 📂 Project Structure

```text
security-log-analyzer/
│
├── app.py
├── analyzer.py
├── sample_logs.csv
├── requirements.txt
├── README.md
├── .gitignore
└── reports/

▶️ How to Run
Install the required packages:
python -m pip install -r requirements.txt

Run the application:
python -m streamlit run app.py

The dashboard will normally open at:
http://localhost:8501

📄 Input Format
The application expects a CSV file containing:
timestamp
ip_address
username
status
event

Example:
2026-10-04 08:15:30,192.168.1.15,user1,FAILED,Invalid password

🔐 Security Note
The sample log data included in this project is synthetic and is intended for educational purposes.

📚 Skills Demonstrated
- Python programming
- Security log analysis
- Authentication monitoring
- Brute-force detection
- Data analysis with Pandas
- Dashboard development with Streamlit
- Data visualization
- Git version control

👩‍💻 Author
Viloshini Peragasam
AI & Cybersecurity Student