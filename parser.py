from os import lseek
from re import T
import requests
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd
import csv


class parse:
    def __init__(self):
        self.url = 'https://robinhood100.com/'

    def parse(self):
        with open('tickers.csv', mode='w') as file:
            writer = csv.writer(file)
            r = requests.get(self.url).text
            soup = BeautifulSoup(r, 'html.parser')
            table = soup.find('table', class_='sortable-theme-bootstrap')

            for row in soup.findAll('table')[0].tbody.findAll('tr'):
                first = row.findAll('td')[2].contents
                writer.writerow(first)



                
            

        



        
f = parse()
f.parse()



