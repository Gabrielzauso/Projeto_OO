from etl_base import EtapaETL
import pandas as pd
import requests as rq

class ExtratorCSV(EtapaETL):
    def __init__(self, caminho, delimitador=";"):
        self.__caminho = caminho
        self.__delimitador = delimitador

    def executar(self, dados=None):
        print("[ExtratorCSV] Lendo arquivo CSV")
        df = pd.read_csv(self.__caminho, sep=self.__delimitador)
        return df
    
class ExtratorAPI(EtapaETL):
    def __init__(self, url):
        self.__url = url

    def executar(self, dados=None):
        print(f"[ExtratorAPI] Fazendo requisição para {self.__url}")
        try:
            response = rq.get(self.__url)
            response.raise_for_status()
            status_code = response.status_code
            print(f"[{__class__.__name__}] Status da requisição: {status_code}")
            data = response.json()
            df = pd.DataFrame(data)
            return df
        except rq.exceptions.RequestException as e:
            print(f"[{__class__.__name__}] Status da requisição: {e}")
        except ValueError as e:
            print(f"Erro ao converter JSON: {e}")