from typing import Union
import unittest
import sys

sys.path.append("..\src")

from breath_data.bd_acess_point.graph_querier import GraphQuerier

class TestGraphQuerier(unittest.TestCase):

    def test_connection(self):
        graph_querier = GraphQuerier()
        graph_querier.close()

    def test_insertion(self):
        graph_querier = GraphQuerier()

        query = (
        "CREATE (p1:Person { name: 'Alice' }) "
        "CREATE (p2:Person { name: 'Jose' }) "
        "CREATE (p1)-[:KNOWS]->(p2) "
        "RETURN p1, p2"
        )
        

            
        sucess, result = graph_querier.query(query)

        self.assertTrue(sucess)
        self.assertEqual(result, [{'p1': 'Alice', 'p2': 'Jose'}])

        graph_querier.close()