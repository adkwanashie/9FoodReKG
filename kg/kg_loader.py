# -----------------------------------------------------
# Food Regulations KG Loader — kg_loader.py
# -----------------------------------------------------
import os
from neo4j import GraphDatabase, Query
from dotenv import load_dotenv
load_dotenv()


from neo4j import GraphDatabase
# -----------------------------------------------------
# Connection Setup
# -----------------------------------------------------
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# -----------------------------------------------------
# Utility Functions
# -----------------------------------------------------
def run_query(query: str, parameters=None):
    """Run a Cypher query and return results as list of dicts."""
    with driver.session(database=NEO4J_DATABASE) as session:
        result = session.run(Query(query), parameters or {}) # type: ignore
        return [record.data() for record in result]

def load_cypher_file(path: str):
    """Load and execute Cypher statements from a .cql file."""
    with driver.session(database=NEO4J_DATABASE) as session:
        with open(path, "r", encoding="utf-8") as f:
            queries = f.read().split(";")
            for query in queries:
                cleaned = query.strip()
                if cleaned:
                    session.run(Query(cleaned)) # type: ignore

def reload_foodregkg():
    """Reload the combined Food Regulations KG from FoodReKG.cql."""
    filepath = os.path.join(os.path.dirname(__file__), "FoodReKG.cql")
    load_cypher_file(filepath)
    print("FoodReKG.cql loaded into Neo4j.")

def close_connection():
    """Close the Neo4j driver connection."""
    driver.close()