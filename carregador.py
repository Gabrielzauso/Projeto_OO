from etl_base import EtapaETL
import json
import pandas as pd

class CarregadorCSV(EtapaETL):
    def __init__(self, caminho_saida):
        self.__caminho_saida = caminho_saida  # Encapsulamento

    def executar(self, dados):
        print(f"[CarregadorCSV] Salvando dados em {self.__caminho_saida}")
        dados.to_csv(self.__caminho_saida)
        return dados