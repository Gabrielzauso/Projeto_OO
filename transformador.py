from abc import ABC, abstractmethod
from etl_base import EtapaETL


class TransformadorMaiusculo(EtapaETL):
    def __init__(self, coluna):
        self.__coluna = coluna

    def executar(self, dados):
        print("[TransformadorMaiusculo] Iniciando processo de Transformar em maiúsculo")
        dados[self.__coluna] = dados[self.__coluna].str.upper()
        return dados
    
class TransformadorRemoverEspacos(EtapaETL):
    def __init__(self, coluna):
        self.__coluna = coluna

    def executar(self, dados):
        print("[TransformadorRemoverEspacos] Iniciando processo de Remover espaços")
        dados[self.__coluna] = dados[self.__coluna].str.strip()
        return dados

    