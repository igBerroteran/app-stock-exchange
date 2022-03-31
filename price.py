
from symtable import Symbol
from typing import AnyStr
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of differences options!
""")





#selected_element = ("Symbol", ("^TYX", "^IXIC", "^GSPC", "^DJI", "MCD", "GE", "BTC-USD", "ETH-USD"))

selected_element2 = st.selectbox("Symbol", ("Treasury Yield 30 Years", "NASDAQ", "S&P 500", "Dow Jones", "McDonalds", "General Electric", "BTC", "ETH"))

#symbol = selected_element2
selected_element2
#st.write(selected_element)

if selected_element2 == "Treasury Yield 30 Years":
    symbol = "^TYX"
elif selected_element2 == "NASDAQ":
    symbol = "^IXIC"
elif selected_element2 == "S&P 500":
     symbol = "^GSPC"
elif selected_element2 == "Dow Jones":
    symbol = "^DJI"
elif selected_element2 == "McDonalds":
    symbol = "MCD"
elif selected_element2 == "General Electric":
    symbol = "GE"
elif selected_element2 == "Dow Jones":
    symbol = "^IXIC"
elif selected_element2 == "BTC":
    symbol = "BTC-USD"
elif selected_element2 == "ETH":
    symbol = "ETH-USD"
            







# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = (symbol)
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-3-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
