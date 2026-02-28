import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Dashboard: AAPL vs MSFT")

tickers = ["AAPL", "MSFT"]
start_date = st.date_input("Start date", value=pd.to_datetime("2023-01-01"))

window = st.slider("Moving Average Window (days)", min_value=5, max_value=200, value=50)

# Download data for both tickers
data = yf.download(tickers, start=str(start_date))

# yfinance returns columns like: ('Close','AAPL'), ('Close','MSFT') when multiple tickers are used
close = data["Close"].copy()

# Moving average for each ticker
ma = close.rolling(window=window).mean()

st.subheader("Close Price")
st.line_chart(close)

st.subheader(f"{window}-Day Moving Average")
st.line_chart(ma)

st.subheader("Close + Moving Average (combined)")
combined = close.join(ma, lsuffix="_Close", rsuffix=f"_MA{window}")
st.line_chart(combined)