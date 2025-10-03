import pandas as pd

class CsvProcessor: # CLASSE
    def __init__(self, arq_caminho: str):
        """Carrega a localização do arquivo"""
        self.arquivo = arq_caminho
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self): # MÉTODO
        """Carrega arquivo para o dataframe pandas"""
        self.df = pd.read_csv(self.arquivo)

    def filtrar_estado(self, estado: str):
        """Filtra por Estado"""
        return self.df[self.df['estado'] == estado]

    def filtrar_por(self, coluna: str, valor: str):
        """Filtro gerenerico que solicita Coluna e Condiçao para o filtro"""
        self.df_filtrado = self.df[self.df[coluna] == valor]
        return self.df_filtrado

    def sub_filtro(self, coluna: str, valor: str):
        """SubFiltro gerenerico aplicado sobre o primeiro filtro"""
        return self.df_filtrado[self.df_filtrado[coluna] == valor]

    def novo_filtrar_por(self, colunas: list, valores: list, df_para_filtrar=None):
        """Filtro gerenerico que recebe listas para o filtro"""
        if len(colunas) != len(valores):
            raise ValueError("Não tem o mesmo numero de colunas e valores")
        
        # Na primeira chamada, usa self.df; nas recursivas, usa o dataframe já filtrado
        df_atual = df_para_filtrar if df_para_filtrar is not None else self.df

        if len(colunas) == 0:
            return df_atual
        
        coluna_atual = colunas[0]
        valor_atual = valores[0]

        # Aplica filtro no dataframe ATUAL
        df_filtrado = df_atual[df_atual[coluna_atual] == valor_atual]

        print(f"############  {coluna_atual} | {valor_atual}\n{df_filtrado}") ## SOMENTE PARA MOSTRAR A FILTRAGEM OCORRENDO

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.novo_filtrar_por(colunas[1:], valores[1:], df_filtrado) # AO CHAMAR NOVAMENTE O METODO ELE AVANÇA 1 POSIÇAO DA LISTA ATE CONCLUIR 
    

if __name__ == "__main__":
    arquivo_csv = 'data/exemplo.csv'
    filtro = 'estado'
    limite = 'SP'

    arquivo_CSV = CsvProcessor(arquivo_csv)
    arquivo_CSV.carregar_csv() # Carrega o csv

    print(arquivo_CSV.filtrar_por(filtro, limite))

    print("##### PRINT DO SUBFILTRO #####")
    print(arquivo_CSV.sub_filtro('preço', '10,50'))

    print("##### PRINT DO DF COM O PRIMEIRO FILTRO #####")
    print(arquivo_CSV.df_filtrado) # Mostra que a alteraçao nao fica permanente, apenas aque foi executada internamente na class

    print("##### PRINT DO DF SEM FILTRO #####")
    print(arquivo_CSV.df)

    # arquivo_csv2 = 'exemplo2.csv'
    # limite2 = 'DF'
    # 
    # arquivo_CSV2 = CsvProcessor(arquivo_csv2)
    # arquivo_CSV2.carregar_csv()
    # 
    # print(arquivo_CSV2.filtrar_por(filtro, limite2))