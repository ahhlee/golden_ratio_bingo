#Python 3

import random
import pandas as pd
import numpy as np

freespace='Free Space'

# Read the CSV into pandas data frame (df)
df = pd.read_csv('grbingo.csv', header=None)

#Make list of 24 randomly generated numbers
numlist = []
while len(numlist)<25:
     r=random.randint(0,len(df)-1)
     if r not in numlist: numlist.append(r)
          
#Make list of bingo options
bingo = []
for i in range(len(numlist)):
    options=df.iloc[i][0]
    if i == 13:
      bingo.append(freespace)
    else:
      bingo.append(options)
    

print(bingo)
