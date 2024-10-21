import numpy as numpy
import pandas as pandas
import matplotlib.pyplot as plt
import yfinance as yf

start = '2012-01-01'
end = '2022-12-21'
stock = 'OKLO'

data = yf.download(stock, start, end)


print(data)