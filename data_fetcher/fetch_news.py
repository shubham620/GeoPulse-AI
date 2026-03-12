import requests

API_KEY = "a4fbec0909a4442b911ef550476788dc"

def fetch_news():

    url = f"https://newsapi.org/v2/everything?q=geopolitics&language=en&apiKey={API_KEY}"

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
