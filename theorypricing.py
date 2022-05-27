import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf
import matplotlib.pyplot as plt





class maths:
    def __init__(self,) -> None:
        self.N = norm.cdf
        
    # These are for the black-scholes model of a european call and put
    def BS_Call(self, S, K, r, T, sig):
        d1 = (np.log(S/K) + r +(sig**2)/2)/(sig*np.sqrt(T))
        d2 = d1 - sig*np.sqrt(T)
        return S * self.N(d1) - self.N(d2)*K*np.exp(-r*T)

    def BS_Put(self, S, K, T, r, sigma):
        d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma* np.sqrt(T)
        return K*np.exp(-r*T)* self.N(-d2) - S* self.N(-d1)

    def historicals(self,ticker, per):
        tickerInfo = yf.Ticker(ticker)
        self.data = tickerInfo.history(period=per)
    # for purposes
    def population(self,ticker,strike):
        self.hist = yf.download(ticker, start='2015-1-1', end='2022-01-01')
        self.hist['log_return'] = np.log(self.hist['Close'] / self.hist['Close'].shift(1))
        self.hist['Volatility'] = self.hist['log_return'].rolling(window=252).std() * np.sqrt(252) 
        self.hist = self.hist[252:]
        stupidlist = []
        self.hist = self.hist.reset_index()

        self.hist['TimeToExperation'] = (self.hist['Date'].dt.dayofweek + 4 - 30 ) * -1
        # this is hardcoded pls remember, it adds 4 days. WILL NOT SCALE BRO
        #self.hist['TimeToExperation'] = self.hist['Date']

        self.hist['Monthly Call Price: ' + str(strike)] = maths().BS_Call(self.hist['Low'], strike,
                                         0,self.hist['TimeToExperation'],self.hist['Volatility'])
        return self.hist


class theorypricing(maths):
    def __init__(self) -> None:
        super().__init__(self)
    def optionPrice(ticker, CP):
        if CP == 'C':
            data = maths().stock_volatility(ticker)
            price = maths().BS_Call(data)
        elif CP == 'P':
            data = maths().stock_volatility(ticker)
            price = maths().BS_Put(data)
        else:
            print("Unrecognizable string")
        return(price)

    
#awe = maths().stock_volatility('SPY')
option = maths().population('SPY', 400)
print(option)
plt.xlabel("time")
plt.ylabel("option price")
plt.title("Graph kuuuun")
plt.plot(option["Monthly Call Price: 400"])
plt.plot(option['Low'])
plt.show()
#re = theorypricing.optionPrice('SPY','C')


    
