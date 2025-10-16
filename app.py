from flask import Flask, render_template, request, jsonify
import yfinance as yf
from groq import Groq
import json
from datetime import datetime, timedelta

app = Flask(__name__)

# Initialize Groq client with API key
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

def get_stock_data(symbol):
    """Fetch stock data using yfinance"""
    try:
        stock = yf.Ticker(symbol)
        
        # Get historical data for the last 30 days
        hist = stock.history(period="1mo")
        
        # Check if we got any data
        if len(hist) == 0:
            return {'error': f'No data available for symbol {symbol}. Please check if the symbol is correct.'}
        
        # Get stock info
        info = stock.info
        
        # Validate that we have actual stock data
        if not info or 'symbol' not in info:
            return {'error': f'Invalid stock symbol: {symbol}'}
        
        # Calculate basic metrics
        current_price = hist['Close'].iloc[-1] if len(hist) > 0 else None
        previous_price = hist['Close'].iloc[-2] if len(hist) > 1 else None
        price_change = current_price - previous_price if current_price and previous_price else 0
        price_change_percent = (price_change / previous_price * 100) if previous_price else 0
        
        # Get volume data
        avg_volume = hist['Volume'].mean() if len(hist) > 0 else 0
        current_volume = hist['Volume'].iloc[-1] if len(hist) > 0 else 0
        
        # Get high and low
        week_high = hist['High'].max() if len(hist) > 0 else 0
        week_low = hist['Low'].min() if len(hist) > 0 else 0
        
        stock_data = {
            'symbol': symbol.upper(),
            'company_name': info.get('longName', info.get('shortName', symbol.upper())),
            'current_price': round(current_price, 2) if current_price else 'N/A',
            'price_change': round(price_change, 2) if price_change else 0,
            'price_change_percent': round(price_change_percent, 2) if price_change_percent else 0,
            'volume': int(current_volume) if current_volume else 0,
            'avg_volume': int(avg_volume) if avg_volume else 0,
            'week_high': round(week_high, 2) if week_high else 0,
            'week_low': round(week_low, 2) if week_low else 0,
            'market_cap': info.get('marketCap', 'N/A'),
            'pe_ratio': info.get('trailingPE', 'N/A'),
            'dividend_yield': info.get('dividendYield', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A'),
        }
        
        return stock_data
    except Exception as e:
        return {'error': str(e)}

def analyze_with_llm(stock_data):
    """Use Groq LLM to analyze stock data and provide structured insights"""
    try:
        # Create a prompt for structured analysis
        prompt = f"""
You are a professional stock analyst. Analyze the following stock data and provide a structured analysis:

Stock: {stock_data['symbol']} - {stock_data['company_name']}
Current Price: ${stock_data['current_price']}
Price Change: ${stock_data['price_change']} ({stock_data['price_change_percent']}%)
30-Day High: ${stock_data['week_high']}
30-Day Low: ${stock_data['week_low']}
Volume: {stock_data['volume']:,}
Average Volume: {stock_data['avg_volume']:,}
Market Cap: {stock_data['market_cap']}
P/E Ratio: {stock_data['pe_ratio']}
Sector: {stock_data['sector']}
Industry: {stock_data['industry']}

Please provide a structured analysis with the following sections:
1. Price Trend Analysis (2-3 sentences)
2. Volume Analysis (1-2 sentences)
3. Valuation Assessment (2-3 sentences)
4. Risk Factors (2-3 bullet points)
5. Overall Recommendation (BUY/HOLD/SELL with brief justification)

Keep the analysis professional, concise, and data-driven.
"""

        # Call Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional stock market analyst providing clear, structured, and actionable insights."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",  # Using Groq's latest model
            temperature=0.7,
            max_tokens=1024
        )
        
        analysis = chat_completion.choices[0].message.content
        return analysis
        
    except Exception as e:
        return f"Error in LLM analysis: {str(e)}"

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze stock based on symbol"""
    try:
        data = request.get_json()
        symbol = data.get('symbol', '').strip().upper()
        
        if not symbol:
            return jsonify({'error': 'Please provide a stock symbol'}), 400
        
        # Get stock data
        stock_data = get_stock_data(symbol)
        
        if 'error' in stock_data:
            return jsonify({'error': f'Could not fetch data for {symbol}. Please check the symbol and try again.'}), 400
        
        # Get LLM analysis
        llm_analysis = analyze_with_llm(stock_data)
        
        # Combine data and analysis
        result = {
            'stock_data': stock_data,
            'analysis': llm_analysis
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
