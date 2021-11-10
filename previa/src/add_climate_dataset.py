import pandas as pd
import numpy as np
from Tkinter import Tk 
from tkinter.filedialog import askopenfilename
from realtional_querier import RelationalQuerier
from graph_querier import GraphQuerier

renamed_columns = ['data','hora','precipitacao total,horario (mm)','pressao atmosferica ao nivel da estacao (mb)','pressao atmosferica max. na hora ant. (aut) (mb)','pressao atmosferica min. na hora ant. (aut) (mb)','radiation (kj/m2)','temperatura do ar - bulbo seco (°c)','temperatura do ponto de orvalho (°c)','temperatura maxima na hora ant. (aut) (°c)','temperatura minima na hora ant. (aut) (°c)','temperatura orvalho max. na hora ant. (aut) (°c)','temperatura orvalho min. na hora ant. (aut) (°c)','umidade rel. max. na hora ant. (aut) (%)','umidade rel. min. na hora ant. (aut) (%)','umidade relativa do ar, horaria (%)','vento direcao horaria (gr) (° (gr))','vento rajada maxima (m/s)','vento velocidade horaria (m/s)','region','state','station','station_code','latitude','longitude','height']
renamed_columns_en = ['date','hour','total precipitation (mm)','pressao atmosferica ao nivel da estacao (mb)','atmospheric pressure max. in the previous hour (mb)','atmospheric pressure min. in the previous hour (mb)','radiation (kj/m2)','air temperature - dry bulb (°c)','dew point temperature (°c)','max. temperature in the previous hour (°c)','min. temperature in the previous hour (°c)','dew temperature max. in the previous hour (°c)','dew temperature min. in the previous hour (°c)','relative humidity max. in the previous hour (%)','relative humidity min. in the previous hour (%)','air relative humidity (%)','wind direction (° (gr))','wind rajada maxima (m/s)','wind speed (m/s)','region','state','station','station_code','latitude','longitude','height']
abbreviation = ['date','hour','prcp', 'stp', 'smax', 'smin','gbrd','temp','dewp','tmax','tmin','dmax','dmin','hmax','hmin','hmdy','wdct', 'gust', 'wdsp', 'regi','prov','wsnm','inme','lat','lon','elvt']
clean_abbreviation = ['prcp', 'stp', 'smax', 'smin','gbrd','temp','dewp','tmax','tmin','dmax','dmin','hmax','hmin','hmdy','wdct', 'gust', 'wdsp', 'regi','prov','wsnm','inme','lat','lon','elvt']

def clean(file_name):
	"""
	! filter raw data from date and stations code
	! process data
	! clean na
	"""
	df = pd.read_csv(file_name)
	print('leu o arquivo')
	
	for i in df.columns:
		df = df.loc[df[i] != -9999]
	print('limpou o arquivo')
	
	df.drop(['index'],inplace=True, axis=1)
	print('indexou o arquivo')
	df.columns = abbreviation
	print('renomeou o arquivo')
	df['date_time'] = pd.to_datetime(df['date'] + ' ' + df['hour'])
	print('juntou a data')
	df.drop(['date', 'hour'], axis=1, inplace=True)
	print('limpou a data')
	df.reset_index(drop=True, inplace=True)
	no.drop(df.columns[0], axis=1, inplace=True)
	print('reindexou o arquivo')
	new_file_name = file_name.split('.')[0]+'_clean.'+file_name.split('.')[1]
	print(new_file_name)
	df.to_csv(new_file_name)
	print('exportou')

	return df, new_file_name

def add_data_graph(df):
	db = GraphQuerier()
	for i in range(len(df)):
		dict = {} 
		for A, B in zip(clean_abbreviation, df[i]):
    		dict[A] = B
		query = 'CREATE (' + i + ':Clima {' + dict + '});'
		result = db.query(query)
		print(len(result))
	db._close()

def add_data_realtional(df):
	db = RelationalQuerier()

	splitted = np.array_split(df, len(df)/100)

	for data in splitted:
		query = 'INSERT INTO Clima VALUES(' + 99*'?,' + '?);'
		result = db.querymany(query, data)
	db.commit()
	print(db.querymany('SELECT * FROM Clima;'))
	print(len(result))
	db._close()

if __name__ == "__main__":

	Tk().withdraw()
	file = askopenfilename()
	print(file)
	df, new_file_name = clean(file)
	print(f'Dasdos tratados estao no arquivo {new_file_name}')

	add_data_relational(df)
	#add_data_graph(df)
