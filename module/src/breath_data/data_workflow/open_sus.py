import sys
import pandas as pd
from relational_querier import RelationalQuerier

def loadcsv() -> pd.DataFrame:
    srag_2013 = pd.read_csv(
        "https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/4919f202-083a-4fac-858d-99fdf1f1d765/download/influd13_limpo_final.csv",
        sep=';', encoding='cp1252', dtype=str)
    srag_2014 = pd.read_csv(
        "https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/2182aff1-4e8b-4aee-84fc-8c9f66378a2b/download/influd14_limpo-final.csv",
        sep=';', encoding='cp1252', dtype=str)
    srag_2015 = pd.read_csv(
        "https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/97cabeb6-f09e-47a5-8358-4036fb10b535/download/influd15_limpo-final.csv",
        sep=';', encoding='cp1252', dtype=str)
    srag_2016 = pd.read_csv(
        "https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/dbb0fd9b-1345-47a5-86db-d3d2f4868a11/download/influd16_limpo-final.csv",
        sep=';', encoding='cp1252', dtype=str)
    srag_2017 = pd.read_csv(
        "https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/aab28b3c-f6b8-467f-af0b-44889a062ac6/download/influd17_limpo-final.csv",
        sep=';', encoding='cp1252', dtype=str)
    srag_2018 = pd.read_csv(
        "https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/a7b19adf-c6e6-4349-a309-7a1ec0f016a4/download/influd18_limpo-final.csv",
        sep=';', encoding='cp1252', dtype=str)
    srag_201314 = srag_2013.merge(srag_2014, how='outer')
    srag_20131415 = srag_201314.merge(srag_2015, how='outer')
    srag_2013141516 = srag_20131415.merge(srag_2016, how='outer')
    srag_201314151617 = srag_2013141516.merge(srag_2017, how='outer')
    srag_20131415161718 = srag_201314151617.merge(srag_2018, how='outer')
    return srag_20131415161718

# Generates a .csv and saves it for quicker reruns
def gencsv():
	srag_full = loadcsv()
	srag_full.to_csv("../resources/srag_full.csv", index=True)
	print("srag_full.csv has been successfully generated")

def add_data_relational(db, df = None, csv = None):

	if df is None and csv is not None:
		df = pd.read_csv(csv)
		i = 0
	for data in df.values:
		i+=1
		query = """
		INSERT INTO SRAG 
		(ID_MUNICIP ,SEM_NOT ,SG_UF_NOT ,DT_SIN_PRI ,DT_NASC ,NU_IDADE_N ,CS_SEXO ,CS_GESTANT ,
		CS_RACA ,CS_ESCOL_N ,SG_UF ,ID_MN_RESI ,ID_OCUPA_N ,VACINA ,FEBRE ,TOSSE ,CALAFRIO ,DISPNEIA ,
		GARGANTA ,ARTRALGIA ,MIALGIA ,CONJUNTIV ,CORIZA ,DIARREIA ,OUTRO_SIN ,OUTRO_DES ,CARDIOPATI ,
		PNEUMOPATI ,RENAL ,HEMOGLOBI ,IMUNODEPRE ,TABAGISMO ,METABOLICA ,OUT_MORBI ,MORB_DESC ,HOSPITAL ,
		DT_INTERNA ,CO_UF_INTE ,CO_MU_INTE ,DT_PCR ,PCR_AMOSTR ,PCR_OUT ,PCR_RES ,PCR_ETIOL ,PCR_TIPO_H ,
		PCR_TIPO_N ,DT_CULTURA ,CULT_AMOST ,CULT_OUT ,CULT_RES ,DT_HEMAGLU ,HEMA_RES ,HEMA_ETIOL ,HEM_TIPO_H ,
		HEM_TIPO_N ,DT_RAIOX ,RAIOX_RES ,RAIOX_OUT ,CLASSI_FIN ,CLASSI_OUT ,CRITERIO ,TPAUTOCTO ,DOENCA_TRA ,
		EVOLUCAO ,DT_OBITO ,DT_ENCERRA ,DT_DIGITA ,SRAG2013FINAL ,OBES_IMC ,OUT_AMOST ,DS_OAGEETI ,DS_OUTMET ,
		DS_OUTSUB ,OUT_ANTIV ,DT_COLETA ,DT_ENTUTI ,DT_ANTIVIR ,DT_IFI ,DT_OUTMET ,DT_PCR_1 ,DT_SAIDUTI ,
		RES_ADNO ,AMOSTRA ,HEPATICA ,NEUROLOGIC ,OBESIDADE ,PUERPERA ,SIND_DOWN ,RES_FLUA ,RES_FLUB ,UTI ,
		IFI ,PCR ,RES_OUTRO ,OUT_METODO ,RES_PARA1 ,RES_PARA2 ,RES_PARA3 ,DESC_RESP ,SATURACAO ,ST_TIPOFI ,
		TIPO_PCR ,ANTIVIRAL ,SUPORT_VEN ,RES_VSR ,RES_FLUASU ,DT_UT_DOSE) 
		VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
		?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
		?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""

		result = db.query(query, data)
		print(i)
	db.commit()

db = RelationalQuerier()

def main():
	if("-gencsv" in sys.argv):
		gencsv()
	try:
		srag_full = pd.read_csv("../resources/srag_full.csv")
	except FileNotFoundError:
		srag_full = loadcsv()

	IBGE = pd.read_csv("../resources/IBGE_Municipios.csv")
	# Uses a dict for optimized city code to city name conversion
	municipdict = {}
	pd.options.mode.chained_assignment = None
	for i in range (len(IBGE['Código Município Completo'])):
		IBGE['Código Município Completo'][i] = str(IBGE['Código Município Completo'][i])[0:6]
		municipdict[IBGE['Código Município Completo'][i]] = IBGE['Nome_Município'][i]

	count = 0
	for i in range(len(srag_full['ID_MUNICIP'])):
		try:
			srag_full['ID_MUNICIP'][i] = municipdict[int(srag_full['ID_MUNICIP'][i])]
		except KeyError:  # If the city code cant be find deletes the line containing it
			print("Erro: Chave " + srag_full['ID_MUNICIP'][i] + " na linha " + str(i) + " nao encontrada, linha sera removida dos dados")
			srag_full.drop(i, inplace = True)
			count = count + 1
	print(str(count) + " linhas foram removidas da tabela pois continham cidades invalidas")

	# Resets index column and removes redundant columns
	srag_full.reset_index(inplace = True)
	srag_full.drop(srag_full.columns[[0, 1]], axis = 1, inplace = True)
	srag_full.drop(['NU_ANO', 'SRAG2014FINAL', 'SRAG2015FINAL', 'SRAG2012FINAL', 'SRAG2017FINAL', 'SRAG2018FINAL'], axis = 1, inplace = True)
	srag_full.to_csv("../resources/srag_full_cities.csv")

	return srag_full

if __name__ == '__main__':

	try:
		srag_full = pd.read_csv("../resources/srag_full_cities.csv")
	except FileNotFoundError:
		main()
	print('adicionando dados')
	add_data_relational(db, df = srag_full)