# To use this program, run the code. Then you will have a file called 'news_data.csv' in the directory.
# that file is the sentiment analysis of the news articles.

import requests
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Getting newspaper data

url = 'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=2f33f4caf615454cac09b7c0d7f38c18'
response = requests.get(url)
news_data = response.json()['articles']
news_content = response.json()

# Initializing the Sentiment Analysis Algorithm and DataFrame instance of the CSV file

sentiment = SentimentIntensityAnalyzer()

# Initaializing a counter for the for loop.

# Creating a CSV file to store the Data
with open('news_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header into the CSV file
    header = ['Topic', 'Negative', 'Neutral', 'Positive', 'Compound']
    writer.writerow(header)

    # Dumping Newspaper data into CSV file
    for data in news_data:

        # Sometimes the news API does not have any content and hence it has None value.
        # This will give a ValueError when working with the data, hence, to get past this we
        # use the try-except block.

        try:
            sent_1 = sentiment.polarity_scores(data['content'])

            # write the data into the CSV file

            writer.writerow([data['title'], sent_1['neg'], sent_1['neu'], sent_1['pos'], sent_1['compound']])

        except ValueError:

            sent_1 = sentiment.polarity_scores(data['title'])
            writer.writerow([data['title'], sent_1['neg'], sent_1['neu'], sent_1['pos'], sent_1['compound']])

        finally:
            continue
