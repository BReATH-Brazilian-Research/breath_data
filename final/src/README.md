# Instruções de uso do dataSUS.py

* o lagoritmo depende dos arquivos `cidades_geo.csv` e `IBGE_Municipios.csv` que devem ser encontrados na mesma pasta `final/src`
* Para ultilizar o script basta digitar o comando `python dataSUS.py` no diretório em que o arquivo se encontra.
* Rodar o script com -gencsv no terminal para gerar a tabela .csv intermediária
* Isso garante uma execução repetida mais rápida pois remove a necessidade de realizar os requests para o dataSUS novamente
* Além disso, após a primeira execução, o código gerará o arquivo `SRAG_full_cities.csv` evitando novas requisições de download e tratamento dos dados para a inserção no banco

# Instruções de uso do dados_climaticos.py

* baixar as tabelas do [kaggle](https://www.kaggle.com/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region) e colocá-las no diretório de sua escolha.

* Executar o script `dados_climaticos.py` em python navegando até a pasta do arquivo e digitando o comando `python dados_climaticos.py`
* Após o início da solução deverá selecionar, pela interface que aparecer, os arquivos de clima dos que foram baixados (`north.csv`, `northeast.csv`, `south.csv`, `southeast.csv`, `center_west.csv` e `stations.csv`).
* O script limpará os dados e os colocará no banco de dados local, além de exportar as tabelas tratadas com o mesmo nome do arquivo de entrada, junto com o prefixo `_clean`.
* Após a primimeira execução, caso queira repopular o banco com estes dados recomenda fazer o mesmo procedimento, mas selecionando os arquivos `north_clean.csv`, `northeast_clean.csv`, `south_clean.csv`, `southeast_clean.csv`, `center_west_clean.csv` e `stations.csv`, evitando o reprocessamento desnecessário dos dados crus.


# Instruções de uso do relational_querier.py

* Este arquivo é apenas para ser chamado pelos demais scripts. ele concentra a interface de comandos para inserção e busca dos dados na criação do BD.
