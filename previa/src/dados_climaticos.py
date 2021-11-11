import pandas as pd
import numpy as np
from Tkinter import Tk 
from tkinter.filedialog import askopenfilename
from realtional_querier import RelationalQuerier
from graph_querier import GraphQuerier

# os dados climaticos brutos foram baixados diretamente do link: https://www.kaggle.com/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region
abbreviation = ['date','precipitacao','pressao_at_max', 'pressao_at_min', 'radiacao', 'temp_max','temp_min','umidade','max_vent','velocidade_vent','region','state','station','lat','lon','elvt']

def clean(file_name):
	"""
	! filter raw data from date and stations code
	! process data
	! clean na
	"""
	df = pd.read_csv(file_name)
	
	for i in df.columns:
		df = df.loc[df[i] != -9999]
	
	preci = df.groupby(['Data'])['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'].sum().reset_index()
	max_pres = df.groupby(['Data'])['PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)'].max().reset_index()
	min_pres = df.groupby(['Data'])['PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)'].min().reset_index()
	rad = df.groupby(['Data'])['RADIACAO GLOBAL (Kj/m²)'].mean().reset_index()
	temp_max = df.groupby(['Data'])['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'].max().reset_index()
	temp_min = df.groupby(['Data'])['TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)'].min().reset_index()
	umidade = df.groupby(['Data'])['UMIDADE RELATIVA DO AR, HORARIA (%)'].mean().reset_index()
	max_vent = df.groupby(['Data'])['VENTO, RAJADA MAXIMA (m/s)'].max().reset_index()
	vel_vent = df.groupby(['Data'])['VENTO, VELOCIDADE HORARIA (m/s)'].mean().reset_index()
	region = df.groupby(['Data'])['region'].min().reset_index()
	state = df.groupby(['Data'])['state'].min().reset_index()
	station = df.groupby(['Data'])['station'].min().reset_index()
	latitude = df.groupby(['Data'])['latitude'].min().reset_index()
	longitude = df.groupby(['Data'])['longitude'].min().reset_index()
	height = df.groupby(['Data'])['height'].min().reset_index()

	clmns = [preci, max_pres, min_pres, rad, temp_max, temp_min, umidade, max_vent, vel_vent, region, state, station, latitude, longitude, height]
	df_final = reduce(lambda left,right: pd.merge(left,right,on='Data'), clmns)
	df_final.columns = abbreviation

	new_file_name = file_name.split('.')[0]+'_clean.'+file_name.split('.')[1]
	print(new_file_name)

	df_final.to_csv(new_file_name)
	print('exportou')

	return df_final, new_file_name

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

	for data in df:
		query = 'INSERT INTO Clima (date,precipitacao,pressao_at_max, pressao_at_min, radiacao, temp_max,temp_min,umidade,max_vent,velocidade_vent,region,state,station,lat,lon,elvt) VALUES(?);'
		result = db.query(query, data)
	db.commit()
	db._close()

if __name__ == "__main__":

	Tk().withdraw()
	file = askopenfilename()
	print(file)
	df, new_file_name = clean(file)
	print(f'Dasdos tratados estao no arquivo {new_file_name}')

	# only uncomment if you want do use the databses
	#add_data_relational(df)
	#add_data_graph(df)
