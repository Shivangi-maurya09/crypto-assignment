from flask import Flask, jsonify, request
from flask_cors import CORS                # ← STEP 1: import CORS
from services.realtime import get_crypto_price
from services.history import get_historical_data
from utils.error_handler import handle_errors

app = Flask(__name__)

CORS(app)                                  # ← STEP 2: add this line just after app = Flask()

app.register_error_handler(Exception, handle_errors)

@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "message": "MCP server running"}), 200

@app.route("/price")
def price():
    symbol = request.args.get("symbol", "BTC")
    data = get_crypto_price(symbol)

    if data.get("price_usd") is None:
        return jsonify({
            "symbol": symbol.upper(),
            "price": None,
            "message": "Price API limit or unavailable"
        }), 200

    return jsonify(data), 200

@app.route("/history")
def history():
    symbol = request.args.get("symbol", "BTC")
    data = get_historical_data(symbol)

    if "error" in data:
        return jsonify({
            "symbol": symbol.upper(),
            "history": None,
            "message": "Historical data temporarily unavailable"
        }), 200

    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)
