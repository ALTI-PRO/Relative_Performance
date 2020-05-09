import pandas as pd
import numpy as np
import pandas_datareader.data as pdat
import seaborn as sb
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

start_date = datetime.datetime(2010, 1, 2) #YYY-MM-DD
end_date = datetime.datetime(2020, 5, 7)

google = pdat.DataReader("GOOG", 'yahoo', start_date, end_date)        #Defining symbols and Start, Stop date
nasdaq = pdat.DataReader("^IXIC", 'yahoo', start_date, end_date)

g_cc = [google.iloc[x][5] for x in range (len(google))]       #List of closing Prices
n_cc = [nasdaq.iloc[x][5] for x in range (len(nasdaq))]
g_c= google.drop(google.columns[0:5], axis=1)                 #Keeping only the adjusted close price and removing other OHLC data
n_c= nasdaq.drop(nasdaq.columns[0:5], axis=1)


r_p = [g_cc[x]/n_cc[x] for x in range (len(g_cc))] #Relative performance calculation
rolling_mean = pd.DataFrame(r_p).rolling(50).mean() # Converting tha list to pandas dataframe and calculating 50 period SMA of Relative Performance

#Plotting Google and NASDAQ Chart
style.use('dark_background')
plt.figure(figsize=(10,5))
ax1= sb.lineplot(x=g_c.index, y= g_c['Adj Close'], label='Google')
ax2= sb.lineplot(x=n_c.index, y=n_c['Adj Close'], label='NASDAQ')
plt.title("Google and NASDAQ Prices from {} to {}".format(start_date, end_date))
plt.legend()
plt.show()

#Plotting Google Chart
style.use('dark_background')
plt.figure(figsize=(10,5))
ax1= sb.lineplot(x=g_c.index, y= g_cc, label='Google')
plt.title(f"Google and Prices from {start_date} until {end_date}")
plt.legend()
plt.show()


#Plotting Relative Performance with 50 SMA of the relative performance
style.use('dark_background')
plt.figure(figsize=(40,20))
ax1= sb.lineplot(x=g_c.index, y= r_p, label='Google')
ax2= sb.lineplot(x=n_c.index, y=rolling_mean[0], label = 'Moving Average 50')
plt.title("Google and NASDAQ Relative Performance")
plt.legend()
plt.show()
