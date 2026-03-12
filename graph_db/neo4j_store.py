from neo4j import GraphDatabase

URI = "enter your uri"
USERNAME = "enter your username"
PASSWORD = "enter your pass"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


def store_event(country, event, location):

    query = """
    MERGE (c:Country {name:$country})
    MERGE (l:Location {name:$location})
    MERGE (e:Event {type:$event})

    MERGE (c)-[:INVOLVED_IN]->(e)
    MERGE (e)-[:LOCATED_IN]->(l)
    """

    with driver.session() as session:
        session.run(query,
                    country=country,
                    event=event,
                    location=location)
