import sqlite3
from sqlite3.dbapi2 import Cursor, Connection
from typing import Dict, List, Tuple, Union

class RelationalQuerier:
	conn : Connection = None
	c : Cursor = None

	def __init__(self):
		# temporary database
		#self.conn = sqlite3.self.connect(':memory:')

		# this line already checks if the db exists
		RelationalQuerier.conn = sqlite3.connect('breath.db')
		
		# create db cursor
		RelationalQuerier.c = RelationalQuerier.conn.cursor()


		RelationalQuerier.c.execute("""CREATE TABLE IF NOT EXISTS Sintoma(
					Código INT NOT NULL AUTO_INCREMENT,
					Ano INT,
					Mês INT,
					Dia INT,
					Cidade FOREIGN_KEY,
					Tipo TEXT,
					PRIMARY KEY (Código))""")

		RelationalQuerier.c.execute("""CREATE TABLE IF NOT EXISTS PacienteSintoma(
					Paciente FOREIGN_KEY,
					Sintoma FOREIGN_KEY)""")


			# create table usuarios
		RelationalQuerier.c.execute("""CREATE TABLE IF NOT EXISTS Usuários(
					Código INT NOT NULL AUTO_INCREMENT,
					Nome TEXT,
					Idade INT,
					PRIMARY KEY (Código))""")

		RelationalQuerier.c.execute("""CREATE TABLE IF NOT EXISTS Cidades(
					Nome TEXT,
					UF INT,
					Código INT NOT NULL,
					PRIMARY KEY (Código))""")

		RelationalQuerier.c.execute("""CREATE TABLE IF NOT EXISTS Pacientes(
					Código INT NOT NULL AUTO_INCREMENT,
					Sexo TEXT,
					Diagnóstico FOREIGN_KEY,
					PRIMARY KEY (Código))""")

		RelationalQuerier.c.execute("""CREATE TABLE IF NOT EXISTS Diagnósticos(
					Código INT NOT NULL AUTO_INCREMENT,
					Diagnóstico TEXT,
					PRIMARY KEY (Código))""")	
			
			# commit changes
		RelationalQuerier.conn.commit()

	
	def query(self, query:str) -> Tuple[bool, Union[List[Dict[str, str]], None]]:
		"""Executes the desired query and fetch its results if there is any
        """
		result = None
		sucess = True
		
		try:
			result = RelationalQuerier.c.execute(query).fetchall()
			sucess = True
		except Exception:
			pass
		
		return sucess, result 

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