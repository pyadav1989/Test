import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')
df=pd.read_csv("/home/prashant/Desktop/Py4E/MyAllProjectWork/stocks_sentdex/newpart.csv")
df['time']=pd.to_datetime(df['time'],unit='s')
df=df.set_index('time')
del df['id']
df.to_csv("/home/prashant/Desktop/Py4E/MyAllProjectWork/stocks_sentdex/newpart1.csv")

df=pd.read_csv("/home/prashant/Desktop/Py4E/MyAllProjectWork/stocks_sentdex/newpart1.csv",index_col="time",parse_dates=True)
stockSymbol='aapl'
df=df[df.type==stockSymbol.lower()]

_500MA=df['value'].rolling(500).mean()
ax1=plt.subplot(2,1,1)
df['close'].plot(label='Price')
plt.legend()

ax2=plt.subplot(2,1,2,sharex=ax1)
_500MA.plot(label='500MA')
plt.legend()
plt.show()
