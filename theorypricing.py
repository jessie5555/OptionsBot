import numpy as np
import pandas as pd
from scipy.stats import norm
import yfinance as yf




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
    def stock_volatility(self,ticker):
        self.hist = yf.download(ticker, start='2015-1-1', end='2022-01-01')
        self.hist['log_return'] = np.log(self.hist['Close'] / self.hist['Close'].shift(1))
        self.hist['Volatility'] = self.hist['log_return'].rolling(window=252).std() * np.sqrt(252) 
        return self.hist[252:]

    def add_time_till_experation(self, ticker):
        hist = maths().stock_volatility(ticker)
        days = 60
        dumb = np.zeros(len(hist))
        for i in range(len(hist)):
            j = i % 30 
            
        i = 0 
        while i != len(hist):
            for j in range(30,1,-1):
                hist['TimeToExperation'][i] = j
        return hist

    


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
print(maths().add_time_till_experation('SPY'))
#re = theorypricing.optionPrice('SPY','C')


    
