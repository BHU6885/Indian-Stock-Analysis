
from flask import Flask, jsonify, render_template, request
import yfinance as yf

app = Flask(__name__)

STOCKS = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Consultancy Services": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "State Bank of India": "SBIN.NS",
    "LTIMindtree": "LTIM.NS",
    "Bharti Airtel": "BHARTIARTL.NS",
    "Sun Pharma": "SUNPHARMA.NS",
    "ITC": "ITC.NS",
}


@app.route("/")
def home():
    return render_template("index.html", stocks=STOCKS)


@app.route("/get_stock_data", methods=["POST"])
def get_stock_data():
    data = request.get_json(silent=True) or {}
    stock_name = data.get("stock")

    if not stock_name or stock_name not in STOCKS:
        return jsonify({"error": "Please select a valid stock."}), 400

    ticker_symbol = STOCKS[stock_name]

    try:
        stock = yf.Ticker(ticker_symbol)
        history = stock.history(period="1y", interval="1d")
        history = history.dropna(subset=["Close"]).copy()

        if history.empty:
            return jsonify({"error": f"No stock data available for {stock_name}."}), 404

        history["Date"] = history.index.strftime("%Y-%m-%d")

        return jsonify(
            {
                "stock": stock_name,
                "ticker": ticker_symbol,
                "dates": history["Date"].tolist(),
                "prices": history["Close"].astype(float).round(2).tolist(),
            }
        )
    except Exception as exc:
        return jsonify({"error": f"Unable to fetch data for {stock_name}: {exc}"}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
