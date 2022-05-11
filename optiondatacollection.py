from cmath import exp
import robin_stocks.robinhood as rs
import os
robin_usr = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")
rs.login(username=robin_usr,
        password=robin_pass,
        expiresIn=120,
        by_sms=True
)

tsla = rs.options.get_option_historicals('TSLA','2022-05-13' , '800','call' ,interval='hour',span='week', bounds='regular')
print(tsla)