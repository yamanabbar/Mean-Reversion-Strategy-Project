# -*- coding: utf-8 -*-
"""
Created on Thu May  8 09:38:19 2025

@author: abbar
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

msft = pd.read_csv('MSFT.CSV')
aapl = pd.read_csv('AAPL.csv')

msft['Date']=pd.to_datetime(msft['Date'])
aapl['Date']=pd.to_datetime(aapl['Date'])
data=pd.merge(msft,aapl, on='Date')

data.set_index('Date',inplace=True)

data.plot(figsize=(12,6),title='MSFT vs AAPL Adjusted Closing Prices')
plt.ylabel('Price')
plt.xlabel('Date')
plt.grid(True)
plt.show()


data['Spread']=data['MSFT']-data['AAPL']
spread_mean = data['Spread'].mean()
spread_std=data['Spread'].std()

data['Z-Score']=(data['Spread']-spread_mean)/spread_std

fig,ax=plt.subplots(2,1,figsize=(12,8))

ax[0].plot(data.index,data['Spread'],label='Spread(MSFT-AAPL)',color='blue')
ax[0].set_title('Spread:MSFT vs AAPL')
ax[0].set_ylabel('Spread')
ax[0].grid(True)

ax[1].plot(data.index,data['Z-Score'],label='Z-Score',color='red')
ax[1].axhline(0,color='black',linestyle='--')
ax[1].set_ylabel('Z-Score')
ax[1].grid(True)

plt.tight_layout()
plt.show()

entry_threshold = 1.0
exit_threshold = 0.0

data['Signal']=0
data.loc[data['Z-Score']<-entry_threshold,'Signal']=1
data.loc[data['Z-Score']>entry_threshold,'Signal']=-1
data.loc[(data['Z-Score']>-exit_threshold) & (data['Z-Score']<exit_threshold),'Signal']=0
data['Position']=data['Signal'].replace(0,np.nan).ffill()
data['Returns']=data['Position'].shift(1)*(data['MSFT'].pct_change()-data['AAPL'].pct_change())

data['Cumulative Returns'] = (1 + data['Returns'].fillna(0)).cumprod()
plt.figure(figsize=(12,6))
plt.plot(data.index, data['Cumulative Returns'], label='Strategy Cumulative Returns', color='green')
plt.title('Cumulative Returns of Mean Reversion Strategy')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid(True)
plt.legend()
plt.show()

total_return = data['Cumulative Returns'].iloc[-1] - 1
annualized_return = (1 + total_return)**(252 / len(data)) - 1
volatility = data['Returns'].std() * np.sqrt(252)
sharpe_ratio = annualized_return / volatility if volatility != 0 else np.nan

print(f"Total Return: {total_return:.2%}")
print(f"Annualized Return: {annualized_return:.2%}")
print(f"Annualized Volatility: {volatility:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
data.to_excel('mean_reversion_strategy.xlsx')
           