import requests

API_KEY = "NEWS_API_KEY"

def fetch_news():

    url = enter your url={API_KEY}"

    response = requests.get(url)
    data = response.json()

    articles = []

    for article in data["articles"]:

        text = article["title"] + " " + str(article["description"])

        articles.append({
            "text": text,
            "source": article["source"]["name"]
        })

    return articles

