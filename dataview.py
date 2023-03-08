import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Import data
data = pd.read_csv("BC_BTC_prices.2023.03.04.1min.csv", header=None, index_col=0)

# Rename the index column to "Date"
data = data.rename_axis("Date")

# Add headers
data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# Reverse the order of rows in data frame, so that earlier times come first in the data.
data = data.iloc[::-1]

# View last 200 rows of data
dataview = data.tail(1000).copy()
pd.options.display.max_rows = 200
print(dataview)

# Chart price data
fig = go.Figure(data=[go.Candlestick(x=dataview.index, open=dataview['Open'], high=dataview['High'], low=dataview['Low'], close=dataview['Close'])])
fig.update_layout(title='Price', title_x=0.5)
fig.show()
