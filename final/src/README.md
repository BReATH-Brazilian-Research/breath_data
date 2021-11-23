# Instruções de uso do dataSUS.py

* Executar o script em python, juntamente à [tabela do IBGE](http://www.students.ic.unicamp.br/~ra234720/MC536/data/external/IBGE_Municipios.csv), para gerar o .csv com os dados processados do dataSUS
* Rodar o script com -gencsv no terminal para gerar a tabela .csv intermediária
* Isso garante uma execução repetida mais rápida pois remove a necessidade de realizar os requests para o dataSUS novamente

# Instruções de uso do clima.py

* baixar as tabelas de [registros de tempo](https://www.kaggle.com/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region)

* Executar o script `clima.py` em python navegando até a pasta do arquivo e digitando o comando `python clima.py`
* Após o início da solução deverá selecionar, pela interface que aparecer, um dos arquivos de clima dos que foram baixados (`north.csv`, `northeast.csv`, `south.csv`, `southeast.csv`, `center_west.csv`, `stations.csv`).
* O script limpará os dados e os colocará no banco de dados local, além de exportar as tabelas tratadas com o mesmo nome do arquivo de entrada, junto com o prefixo `_clean`.


# Instruções de uso do relational_querier.py

* Estes arquivos são apenas par serem chamados pelos demais scripts


OBS: Alguns do scripts podem não estar funcionando corretamente devido as constantes mudanças neles.
