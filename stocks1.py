from logging import getLoggerClass
import yfinance as yf
import streamlit as st
import pandas as pd
from yfinance import ticker

st.write("""Apple Company stocks from 2010 to 2020""")

tickerSymbol = "AAPL"

tickerdata = yf.Ticker(tickerSymbol)

tickerDf = tickerdata.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
