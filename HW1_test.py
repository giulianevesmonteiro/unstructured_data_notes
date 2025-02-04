

#Importing the packages and data files:
import glob as glob
import pandas as pd
import re

#pd.read_table(data[0], header=None)

#Confirming all files are being read correctly:
#docs = glob.glob(r"C:\Users\Graduate\Documents\ND\Unstructured_Data_Analytics\calls\*")  
#data = []



def read_calls():
    # Use glob to find all text files in the specified folder
    files = glob.glob(r"C:\Users\Graduate\Documents\ND\Unstructured_Data_Analytics\calls\*")
    # Define a list to hold the data
    data = []

    # Regular expressions to extract ticker, quarter, and year
    ticker_pattern = re.compile(r'([A-Z]+)', re.IGNORECASE) #'\b([A-Z]+)\b'
    # Capture a sequence of uppercase letters, that can happen have more than 1 occurence
    quarter_pattern = re.compile(r'Q[1-4]', re.IGNORECASE)
    # Match the letter Q with any digit from 1-4
    year_pattern = re.compile(r'\d{4}')
    # Match any digit (0-9) and specifying we want exactly 4 digits

    # Iterate over each file
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            # Read file content
            content = f.read()

            # Extract ticker (you might need to adjust the regex depending on the file format)
            ticker_search = ticker_pattern.search(content)
            ticker = ticker_search.group(0) if ticker_search else None
            
            # Extract quarter (similar approach)
            quarter_search = quarter_pattern.search(content)
            quarter = quarter_search.group(0).upper() if quarter_search else None
            
            # Extract year
            year_search = year_pattern.search(content)
            year = year_search.group(0) if year_search else None

            # Append extracted data to the list
            data.append({'ticker': ticker, 'quarter': quarter, 'year': year})

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Data cleaning: drop rows with any missing values
    df.dropna(inplace=True)

    return df

# Example usage
# df_calls = read_calls('path/to/calls')
# print(df_calls)
testing = read_calls()

print(testing)


## Step 2

#Use the AlphaVantage api to get daily stock prices for WWE and related tickers for the last 5 years -- pay attention to your data. You cannot use any AlphaVantage packages (i.e., you can only use requests to grab the data). Tell me about the general trend that you are seeing. I don't care which viz package you use, but plotly is solid and plotnine is good for ggplot2 users.

import requests 

## Step 3

#Just like every other nerdy hobby, professional wrestling draws dedicated fans. Wrestling fans often go to cagematch.net to leave reviews for matches, shows, and wrestlers. The following link contains the top 100 matches on cagematch: https://www.cagematch.net/?id=111&view=statistics

#* What is the correlation between WON ratings and cagematch ratings?

#** Which wrestler has the most matches in the top 100?

#*** Which promotion has the most matches in the top 100? 

#**** What is each promotion's average WON rating?

#***** Select any single match and get the comments and ratings for that match into a data frame.


from bs4 import BeautifulSoup



## Step 4

#You can't have matches without wrestlers. The following link contains the top 100 wrestlers, according to cagematch: https://www.cagematch.net/?id=2&view=statistics

#*** Of the top 100, who has wrestled the most matches?

#***** Of the top 100, which wrestler has the best win/loss?


## Step 5

#With all of this work out of the way, we can start getting down to strategy.

#First, what talent should WWE pursue? Advise carefully.

#Second, reconcile what you found in steps 3 and 4 with Netflix's relationship with WWE. Use the data from the following page to help make your case: https://wrestlenomics.com/tv-ratings/

#Third, do you have any further recommendations for WWE?