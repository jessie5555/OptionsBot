import robin_stocks.robinhood as rs
import os
import yfinance as yf
import pandas


class optiondatacollection:
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


    def option(self, ticker):
        # alright so this enumerations kinda weird, I dont want to fix it. But,
        # so the row is a tuple with two things in it, the first is the timestamp
        # and the second is literally THE REST OF THE DATA
        # So you need to iterate through the second tuple as a 2d array. Noted...
        for id, row  in enumerate(self.data.iterrows()):
            
            if id == 0:
                pass
            date = str(row[0]).split(' ')
            date = date[0]
            #date = date.split('-')
            print(date)
            strike = (row[1][0] + row[1][3]) / 2   # this was just a monkey brain way of finding a strike price 
            strike = round(strike/5)*5
            strike = str(strike)
            print(strike)
            
            try: 
                spy = rs.options.get_option_historicals(ticker, date, strike,'call', interval='hour',span='week', bounds='regular')
                print(spy)
                break

            except:
                pass

#Je


rob = optiondatacollection()
rob.test("TSLA", "2022-05-20", "765")
#rob.historicals('SPY', '6mo')
#rob.option('SPY')


