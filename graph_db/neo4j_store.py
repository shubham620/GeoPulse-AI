from neo4j import GraphDatabase

URI = "neo4j+s://a7f5d3f1.databases.neo4j.io"
USERNAME = "a7f5d3f1"
PASSWORD = "wcPxZbrZ5CjQBgFiL7k2M6HT9a5jmZBf5huypDYQAVc"

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
