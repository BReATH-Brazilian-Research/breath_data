import sqlite3
from typing import Dict, List, Tuple, Union

class RelationalQuerier:
	conn = None
	c = None

	def __init__(self):
		# temporary database
		#self.conn = sqlite3.self.connect(':memory:')

		# this line already checks if the db exists
		RelationalQuerier.conn = sqlite3.self.connect('breath.db')
		
		# create db cursor
		RelationalQuerier.c = RelationalQuerier.conn.cursor()


		RelationalQuerier.c.execute("""CREATE TABLE IF NOT EXISTS Sintoma(
				Tipo TEXT,
				Ano INT,
				Mês INT,
				Dia INT,
				Cidade TEXT,
				Paciente FOREIGN_KEY)""")

		RelationalQuerier.c.execute("""CREATE TABLE IF NOT EXISTS PacienteSintoma(
				Paciente FOREIGN_KEY,
				Sintoma FOREIGN_KEY)""")


			# create table usuarios
		RelationalQuerier.c.execute("""CREATE TABLE IF NOT EXISTS Usuarios(
					name TEXT,
					nome TEXT,
					id INT,
					laudo TEXT,
					idade INT,
					estado_civil TEXT)""")
			
			# commit changes
		RelationalQuerier.conn.commit()

	
	def query(self, query:str) -> Tuple[bool, Union[List[Dict[str, str]], None]]:
		"""Executes the desired query and fetch its results if there is any
        """
		return RelationalQuerier.c.execute(query).fetchall()

	def cancel(self):
		"""Close the database connection once the program is done with it.
		"""
		RelationalQuerier.conn.rollback()


	def commit(self):
	   RelationalQuerier.conn.commit()

	def _close(self):
		"""Close the database connection once the program is done with it.
		"""
		RelationalQuerier.conn.close()

	def __del__(self):
		self._close()