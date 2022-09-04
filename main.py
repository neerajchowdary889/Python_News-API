from newsapi import NewsApiClient
import datetime as dt
import pandas as pd
from key import Key

# print(Key)
# Key is the API key to access the data from NewsAPI.
Topic = input("Enter the topic to search on :\n")
newsapi = NewsApiClient(api_key=Key)

data = newsapi.get_everything(q = Topic,language='en', page_size=15)
# , sources="the-verge"
articles = data['articles']

for x, y in enumerate(articles):
    print(f"{x}   {y['title']}")
print(type(data))