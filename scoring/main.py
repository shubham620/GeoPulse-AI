from data_fetcher.fetch_news import fetch_news
from nlp_pipeline.entity_extraction import extract_entities
from event_engine.detect_events import detect_event
from scoring.risk_score import risk_score

def run_pipeline():

    articles = fetch_news()

    for article in articles:

        text = article["text"]

        entities = extract_entities(text)

        event = detect_event(text)

        risk = risk_score(event)

        print("\n---------------------------")
        print("News:", text)
        print("Entities:", entities)
        print("Event Type:", event)
        print("Risk Score:", risk)


if __name__ == "__main__":
    run_pipeline()
