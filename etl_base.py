from abc import ABC, abstractmethod

class EtapaETL(ABC):
    @abstractmethod
    def executar(self, dados):
        pass