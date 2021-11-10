# Instruções de uso do dataSUS.py

* Executar o script em python, juntamente à [tabela do IBGE](http://www.students.ic.unicamp.br/~ra234720/MC536/data/external/IBGE_Municipios.csv), para gerar o .csv com os dados processados do dataSUS
* Rodar o script com -gencsv no terminal para gerar a tabela .csv intermediária
  * Isso garante uma execução repetida mais rápida pois remove a necessidade de realizar os requests para o dataSUS novamente
