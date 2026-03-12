from data_fetcher.fetch_news import fetch_news
from nlp_pipeline.entity_extraction import extract_entities
from event_engine.detect_events import detect_event
from scoring.risk_score import risk_score
from graph_db.neo4j_store import store_event
from event_engine.verify_events import verify_events
import pandas as pd


def run_pipeline():

    articles = fetch_news()

    texts = []  # store news texts for verification
    results = []  # store structured event data

    for article in articles:

        text = article["text"]
        texts.append(text)

        # Extract entities
        entities = extract_entities(text)

        # Detect event type
        event = detect_event(text)

        # Calculate risk
        risk = risk_score(event)

        print("\n---------------------------")
        print("News:", text)
        print("Entities:", entities)
        print("Event Type:", event)
        print("Risk Score:", risk)

        # -----------------------------
        # Extract country and location
        # -----------------------------

        country = None
        location = None

        for entity, label in entities:

            if label == "GPE":   # Country
                country = entity

            if label == "LOC":   # Location
                location = entity

        # -----------------------------
        # Store in Knowledge Graph
        # -----------------------------

        if country and location:
            store_event(country, event, location)
            print("Stored in Graph:", country, event, location)

        # -----------------------------
        # Save event data for dashboard
        # -----------------------------

        results.append({
            "Country": country if country else "Unknown",
            "Event": event if event else "General Event",
            "Risk": risk if risk else 0.1,
            "News": text
        })

    # -----------------------------
    # Save results to CSV
    # -----------------------------

    df = pd.DataFrame(results)
    df.to_csv("events.csv", index=False)

    print("\nSaved events to events.csv")

    # -----------------------------
    # Cross Verification Section
    # -----------------------------

    print("\n==============================")
    print("CROSS VERIFICATION RESULTS")
    print("==============================")

    verified = verify_events(texts)

    if not verified:
        print("No similar events detected in this batch.")

    for news1, news2, score in verified:

        print("\nPossible Same Event Detected")
        print("News 1:", news1)
        print("News 2:", news2)
        print("Similarity Score:", score)


if __name__ == "__main__":
    run_pipeline()