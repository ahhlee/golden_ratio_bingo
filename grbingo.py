#Python 3

import random
import requests
import pandas as pd
from io import StringIO
from tabulate import tabulate


freespace='Free Space'

## Load the bingo options from the linked spreadsheet. 
url= requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQf_1onKJlXJ8KVdnjFU8mQRCz2QfIjsmVzpevFom7DZPvEtgsCRzZnIfl9-YyofQqGILf9RPSAilqg/pub?output=csv')
csv_raw = StringIO(url.text)
df = pd.read_csv(csv_raw, header=None)

## Pull random items from the bingo options
df2=df.sample(n=25)
    
#Make list of bingo options
bingolist = []
for i in range (25):
    options=df2.iloc[i][0]
    if i == 12:
      bingolist.append(freespace)
    else:
      bingolist.append(options)
      
row1=bingolist[0:5]
row2=bingolist[5:10]
row3=bingolist[10:15]
row4=bingolist[15:20]
row5=bingolist[20:25]

table=[row1,row2,row3,row4,row5]

bingo=tabulate(table, headers=["B","I","N","G","O"], tablefmt="grid", maxcolwidths=25)

bingocard = open("grbingocard.txt","w")
bingocard.write(bingo)
bingocard.close()
