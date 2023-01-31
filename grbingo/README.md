# Golden Ratio Bingo

This is a project created for the /r/thegoldenratio4 subreddit as a fun way to play bingo based on content that frequently comes up in social media account about a family of 5 golden retrievers.

The project takes in a Google Sheet with a list of common scenarios that happen to the dogs, such as "Venk did a dance at dinner time". The program randomly selects 24 entries from the spreadsheet, and a "Free Space" and generates a 5 x 5 Bingo Card Grid of scenarios to be checked off.

********************************

## Requirements:
-Python3\
-random\
-requests\
-pandas\
-io\
-tabulate

These modules can be installed via the following commands:
Mac/Linux: \
```brew install python3```\
```pip3 install requests```

Windows:\
You'll need to install the latest version of Python3 from [here](https://www.python.org/downloads/windows/).\
Then run the following command:\
```python -m pip install requests```




*******************************

## To Run:

After cloning the file, use the following command in the terminal to run the program:

On Mac/Linux:\
```python grbingo.py```

If multiple instances of python:\
```python3 grbingo.py```

On Windows:\
```python grbingo.py```

Once the program has successfully run it will create a grbingocard.txt file in the current directory.

*********
### Example Output:


[grbingocard.txt](https://github.com/ahhlee/projects/files/10543569/grbingocard.txt)
