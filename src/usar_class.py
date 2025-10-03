from interface.classes.csv_class import CsvProcessor

arquivo_csv = 'data/exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv() # Carrega o csv

# print(arquivo_CSV.filtrar_por(filtro, limite))
# 
# print("##### PRINT DO SUBFILTRO #####")
# print(arquivo_CSV.sub_filtro('preço', '10,50'))
# 
# print("##### PRINT DO DF COM O PRIMEIRO FILTRO #####")
# print(arquivo_CSV.df_filtrado) # Mostra que a alteraçao nao fica permanente, apenas aque foi executada internamente na class

# print("##### PRINT DO DF SEM FILTRO #####")
# print(arquivo_CSV.df)

filtros: list = ['estado', 'data', 'preço']
valores: list = ['SP', '20/01/2024', '10,50']

print("\n##### PRINT DO FILTRO RECURSIVO #####")
print(arquivo_CSV.novo_filtrar_por(filtros, valores))


# CRIANDO UM NOVO FILTRO E SALVANDO NA MEMORIA df_filtrado E GERANDO UM SUBFILTRO

# arquivo_csv2 = 'exemplo2.csv'
# limite2 = 'DF'
# 
# arquivo_CSV2 = CsvProcessor(arquivo_csv2)
# arquivo_CSV2.carregar_csv()
# 
# print(arquivo_CSV2.filtrar_por(filtro, limite2))