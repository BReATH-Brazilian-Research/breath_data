# keep reading from here https://neo4j.com/docs/python-manual/current/cypher-workflow/
# docs https://neo4j.com/docs/api/python-driver/4.3/api.html#api-documentation
# this works with a local neo4j, but we can make a server later
from neo4j import ( GraphDatabase, TRUST_ALL_CERTIFICATES)
import logging
from neo4j.exceptions import ServiceUnavailable

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logging.getLogger("neo4j").addHandler(handler)

class GraphDB:

	def __init__(self):
		self.driver = GraphDatabase.driver(
			"bolt://localhost:7687", auth=("neo4j","password"))#,
			# max_connection_lifetime=30 * 60,
			# max_connection_pool_size=50,
			# connection_acquisition_timeout=2 * 60,
			# connection_timeout=15,
			# encrypted=True,
			# trust=TRUST_ALL_CERTIFICATES)

	def close(self):
		# Don't forget to close the driver connection when you are finished with it
		self.driver.close()

	def query(self, query = None):
		# To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
		# The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/

		result = self.driver.session().run(query)
		try:
			return [{"p1": row["p1"]["name"], "p2": row["p2"]["name"]}
					for row in result]
		# Capture any errors along with the query and data for traceability
		except ServiceUnavailable as exception:
			logging.error("{query} raised an error: \n {exception}".format(
				query=query, exception=exception))
			raise

if __name__ == "__main__":
	bolt_url = "bolt://localhost:7687"
	user = "neo4j"
	password = "password"
	GraphDB = GraphDB()
	query = (
	"CREATE (p1:Person { name: 'Alice' }) "
	"CREATE (p2:Person { name: 'Jose' }) "
	"CREATE (p1)-[:KNOWS]->(p2) "
	"RETURN p1, p2"
	)
	GraphDB.query()
	GraphDB.close()