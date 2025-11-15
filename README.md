🚀 Crypto Market Data MCP Server

A simple Python-based MCP server and frontend dashboard that fetches real-time and historical cryptocurrency data using public APIs.

📌 Features
🔹 Backend (Flask + CCXT)

/ping → Server health check

/price?symbol=BTC → Real-time crypto price

/history?symbol=BTC → Last 24 hours historical OHLCV data

Caching implemented using cachetools

Fully structured services + utils architecture

Included pytest tests for API validation

🔹 Frontend (HTML + CSS + JavaScript)

A simple crypto dashboard with:

Dropdown to select coin (BTC, ETH, BNB, SOL)

Shows live price

Displays a 24-hour chart using Chart.js

Fetches data from the Flask backend APIs

📁 Project Structure
crypto-assignment/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── services/
│   │     ├── realtime.py
│   │     ├── history.py
│   ├── utils/
│   │     ├── cache.py
│   │     ├── error_handler.py
│   ├── tests/
│         ├── test_app.py
│
└── frontend/
    ├── index.html
    ├── style.css
    ├── script.js

⚙️ Technologies Used
Backend

Python

Flask

CCXT

Cachetools

Pytest

Frontend

HTML

CSS

JavaScript

Chart.js

▶️ How to Run the Backend

Open terminal inside /backend

Install dependencies:

pip install -r requirements.txt


Run server:

python app.py


Server runs at:
👉 http://127.0.0.1:5000

▶️ Useful Backend Endpoints
Endpoint	Description
/ping	Server check
/price?symbol=BTC	Real-time price
/history?symbol=BTC	24h OHLCV data
▶️ How to Run the Frontend

Just open:

frontend/index.html


It will fetch data automatically from the running backend.

🧪 Tests

To run unit tests:

pytest backend
