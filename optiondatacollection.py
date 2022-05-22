import robin_stocks.robinhood as rs
import os
import yfinance as yf
import pandas as pd

# I dont know if I want to do this yet....
class date:
    def __init__(self,year, month, day):
       pass 


class optiondatacollection():
    def __init__(self):
        self.robin_usr = os.environ.get("robinhood_username")
        self.robin_pass = os.environ.get("robinhood_password")
        rs.login(username=self.robin_usr,
                password=self.robin_pass,
                expiresIn=500,
            by_sms=True
        )
    #def tickers(self):

    def time(year, month, day):
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)

        string = str(year) + '-' + str(month) + '-' + str(day)
        return string

    def historicals(self,ticker, per):
        tickerInfo = yf.Ticker(ticker)
        self.data = tickerInfo.history(period=per)

    def test(self, ticker, date, strike):
        teststock = rs.options.get_option_historicals(ticker, date, strike, "call", interval="hour", span="week", bounds="regular")
        print(teststock)

    def Rebecca_Black(self, year): # returns all fridays in a year, this was an appropriate function name trust me
        #you know what this is my project, Im doing this for fun! I dont have to obey any standards. This is going to work so well
        # that I wont need a job anyway! hahah checkmate future employer. not that youre going to read this anyway.
        return pd.date_range(start=str(year), end=str(year+1),
                freq='W-FRI').strftime('%m/%d/%Y').tolist()[:52]  # also I stole this code thanks:https://gist.github.com/isaacarnault/7c87a09ce6adc0d88f245037b3bbd56c

