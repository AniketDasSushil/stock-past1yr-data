import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Stock Data founder')
st.subheader('type ".ns" after every stock ticker')
n = st.number_input('type the number of ticker',min_value=1,
                   max_value=10)
n = int(n)
ticker = []
weight = []
for i in range(0,n):
    name = st.text_input(f'type the name of the stock:- {i}')
    #w = st.number_input(f'type the weight of {i}')
    ticker.append(name)
    #weight.append(w)
@st.cache(suppress_st_warning=True)
def run(ticker):
    df = yf.download(ticker,period='1y')['Adj Close']
    plt.plot(df)
    plt.legend(df)
    fig = plt.show()
    st.pyplot(fig)
btn = st.button('Run')
if btn:
    run(ticker)
    