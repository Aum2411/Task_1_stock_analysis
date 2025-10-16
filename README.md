# 🤖 AI Stock Analysis Agent

A powerful stock analysis tool that combines real-time market data with AI-powered insights using Groq LLM.

## 📚 Documentation

📖 **[DOCUMENTATION.md](DOCUMENTATION.md)** - Complete guide (setup, usage, how it works, troubleshooting) - 3-4 pages

## Features

- **Real-time Stock Data**: Fetches live stock prices, volume, and market metrics using yfinance
- **AI-Powered Analysis**: Uses Groq's LLM (Llama 3.1 70B) for intelligent stock analysis
- **Structured Insights**: Get organized analysis with price trends, volume analysis, valuation, risks, and recommendations
- **Beautiful UI**: Modern, responsive web interface with gradient design
- **Easy to Use**: Simply enter a stock symbol and get comprehensive analysis instantly

## Technologies Used

- **Backend**: Python, Flask
- **Data**: yfinance (Yahoo Finance API)
- **AI**: Groq API with Llama 3.1 70B model
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with gradient design

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter a stock symbol (e.g., AAPL, TSLA, MSFT, GOOGL)
2. Click "Analyze Stock" or press Enter
3. View comprehensive stock data and AI-generated analysis

## Sample Stock Symbols

Try these popular stocks:
- **AAPL** - Apple Inc.
- **MSFT** - Microsoft Corporation
- **GOOGL** - Alphabet Inc. (Google)
- **TSLA** - Tesla, Inc.
- **AMZN** - Amazon.com, Inc.
- **META** - Meta Platforms, Inc.
- **NVDA** - NVIDIA Corporation

## API Information

This application uses:
- **Groq API**: For AI-powered stock analysis
- **yfinance**: For real-time stock market data

## Project Structure

```
Task_1/
├── app.py              # Flask backend server
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── templates/
│   └── index.html     # Main HTML interface
└── static/
    └── style.css      # CSS styling
```

## Features Breakdown

### Stock Data Metrics
- Current price and daily change
- 30-day high/low prices
- Trading volume and average volume
- Market capitalization
- P/E ratio
- Sector and industry information

### AI Analysis Sections
1. **Price Trend Analysis**: Insights on stock price movements
2. **Volume Analysis**: Trading activity interpretation
3. **Valuation Assessment**: Company valuation evaluation
4. **Risk Factors**: Potential risks to consider
5. **Overall Recommendation**: BUY/HOLD/SELL suggestion with justification

## Notes

- The Groq API key is embedded in the code for convenience
- Stock data is fetched in real-time from Yahoo Finance
- Analysis is generated on-demand for each query
- The app runs on port 5000 by default

## License

This project is open source and available for educational purposes.
