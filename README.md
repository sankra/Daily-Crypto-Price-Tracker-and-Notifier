# Daily-Crypto-Price-Tracker-and-Notifier

# 🪙 Crypto Price Tracker with Apache Airflow

Track daily cryptocurrency prices (Bitcoin & Ethereum) using Apache Airflow and get notified when prices exceed a threshold. This gives a notification to find the price.

---

## 📌 Project Overview

This project demonstrates the use of **Apache Airflow** for orchestrating a data pipeline in Python. It fetches real-time crypto prices using the [CoinGecko API](https://www.coingecko.com/en/api), saves them as CSV, and optionally sends a notification if the price of Ethereum exceeds a threshold. Project involves other taks that can be peformed using Apache Airflow.

---

## 🧰 Tech Stack

- **Apache Airflow**
- **Python 3.8**
- **CoinGecko API**
- **Docker (Optional if you are not able to run airflow in your machine)**
- **XCom / Branching / Sensors / Notifications**


---

## 📂 Project Structure
crypto_airflow_project/
├── dags/
│   └── crypto_price_dag.py
├── plugins/
│   └── custom_operator.py
├── data/
│   └── prices/
├── requirements.txt
├── README.md
└── docker-compose.yml  # Optional for local Airflow setup

