from abc import ABC, abstractmethod

class EtapaETL(ABC):
    @abstractmethod
    print('teste')
    def executar(self, dados):
        pass