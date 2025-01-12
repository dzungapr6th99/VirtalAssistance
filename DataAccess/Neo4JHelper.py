from langchain_community.graphs import Neo4jGraph
from typing import TypeVar, Callable
from neo4j import GraphDatabase
import logging
T = TypeVar('T', bound = object)

class Neo4JHelper:
    def __init__(self, uri: str, user: str, password: str, graph: Neo4jGraph):
        self._graph = graph
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def AddNode(self, func: Callable[[T], None], data: T) -> None:
        logging.info(msg = 'start insert Node with data ', object= data)
        with self._driver.session() as session:
            session.write_transaction(data)
            
    