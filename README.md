🚀 Crypto Market Data MCP Server

A Python-based backend + frontend system that fetches real-time and historical cryptocurrency data using public APIs.
Includes a lightweight dashboard built with HTML, CSS, and JavaScript.

🔥 Features
🖥️ Backend (Flask + CCXT)

/ping → Server health check

/price?symbol=BTC → Real-time cryptocurrency price

/history?symbol=BTC → Last 24 hours OHLCV historical data

In-memory caching using cachetools

Clean architecture with services + utils modules

Integrated pytest tests for API validation

🎨 Frontend (HTML + CSS + JavaScript)

Modern UI crypto dashboard

Dropdown to select coin (BTC, ETH, BNB, SOL)

Displays:

Live price

24-hour chart (Chart.js)

Automatically fetches data from backend APIs

📂 Folder Structure
crypto-assignment/
│── backend/
│   ├── app.py
│   ├── services/
│   │   ├── realtime.py
│   │   └── history.py
│   ├── utils/
│   │   ├── cache.py
│   │   └── error_handler.py
│   ├── tests/
│   │   └── test_app.py
│   └── requirements.txt
│
│── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── README.md

⚙️ How to Run the Project
▶️ 1. Backend Setup
cd backend
pip install -r requirements.txt
python app.py


Backend will start on:
👉 http://127.0.0.1:5000

▶️ 2. Frontend Setup

Simply open this file in your browser:

frontend/index.html


No server required.

🛠️ Tech Stack
Backend

Python

Flask

CCXT

Cachetools

Requests

Pytest

Frontend

HTML

CSS

JavaScript

Chart.js

🌟 API Endpoints
Endpoint	Description
/ping	Health check
/price?symbol=BTC	Real-time price
/history?symbol=BTC	24h OHLCV history
💡 Highlights

Clean project architecture

Easy to run and extend

Suitable for learning backend + API integration

Minimalistic crypto dashboard with real data
