import requests
import random
def getNewsHeadline():
    searchParams = ["country=us", "country=gb", "language=en", "category=technology", "category=science", "category=general", "q=president"]
    paramNumber = random.randint(0, len(searchParams) - 1)
    print(searchParams[paramNumber])
    url = ('http://newsapi.org/v2/top-headlines?'
       + searchParams[paramNumber] +
       '&apiKey=280fc146423f4058b6bcafc661c70017')
    response = requests.get(url)
    articleNumber = random.randint(0, len(response.json()["articles"]) - 1)
    return response.json()["articles"][articleNumber]["title"]
