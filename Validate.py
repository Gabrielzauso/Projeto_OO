from etl_base import EtapaETL
import pandas as pd

class Validador_Email(EtapaETL):
    def __init__(self, coluna):
        self.__coluna = coluna

    def executar(self, dados):
        print(f"[{__class__.__name__}] Validando e-mails")
        if not dados[self.__coluna].str.contains("@").all():
            linhas_invalidas = dados[~dados[self.__coluna].str.contains("@")]
            print(f"[ERRO] E-mails inválidos encontrados: {linhas_invalidas[self.__coluna].count()}")
            raise ValueError("Foram encontrados e-mails inválidos (sem '@')")
        return dados