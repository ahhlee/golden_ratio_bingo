#Python 3

import random
import requests
import pandas as pd
from io import StringIO




freespace='Free Space'

# Read the CSV into pandas data frame (df)
#df = pd.read_csv('grbingo.csv', header=None)

url= requests.get('https://docs.google.com/spreadsheets/d/' + 
                   '1BezMJn85XcywGSUkN_KO4_OuTh-8xrtCV6wXwIYOcrs' +
                   '/export?gid=0&format=csv')
csv_raw = StringIO(url.text)
df = pd.read_csv(csv_raw, header=None)

#Make list of 24 randomly generated numbers
numlist = []
while len(numlist)<25:
     r=random.randint(0,len(df)-1)
     if r not in numlist: numlist.append(r)
          
#Make list of bingo options
bingolist = []
for i in range(len(numlist)):
    options=df.iloc[i][0]    
    if i == 12:
      bingolist.append(freespace)
    else:
      bingolist.append(options)
row1=bingolist[0:5]
print(row1)
row2=bingolist[5:10]
row3=bingolist[10:15]
row4=bingolist[15:20]
row5=bingolist[20:25]

table=[row1,row2,row3,row4,row5]

bingo=tabulate(table, headers=["B","I","N","G","O"], tablefmt="fancy_grid")

print(bingo)

