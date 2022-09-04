from newsapi import NewsApiClient
from key import Key

# print(Key)
# Key is the API key to access the data from NewsAPI.

Topic = input("Enter the topic to search on :\n>>>")
newsapi = NewsApiClient(api_key=Key) # We are declaring our key and connecting to the server. If entered key is wrong then it will throw error.

data = newsapi.get_everything(q = Topic,language='en', page_size=20)
# q is query here based on query results will be generated.
# page_size is the number of articles that should be displaced, it can be changed.
# from_param = '2019-06-03' to get the articles from that certain date.
# sources="the-verge" to get the articles from certain source.
articles = data['articles']

print("_______________________________________________________________________________________\n")

for x, y in enumerate(articles):
    print(f"{x}   {y['title']}")

print("\n_______________________________________________________________________________________")

# data is dict here.

def GettingSource():
    sourceinput = int(input("\nEnter the article serial number to get the source: \n>>>"))

    print("______________________________________________________________________________________")
    for Key, value in articles[sourceinput].items():
        print(f"\n {Key.ljust(15)} {value}")
    print("\n______________________________________________________________________________________")

    repeat = int(input("\n1. Read another article \n2. Stop reading \n>>>"))
    if repeat == 1:
        GettingSource()
    elif repeat == 2:
        print("Byee... Have a nice day")
    else :
        raise ("Wrong Input")

getsource = int(input("\nPress '1' to get the source of any of the article listed above or anything else to exit: \n>>>"))

if getsource == 1:

    GettingSource()

else:
    print("Byee... Have a good day")