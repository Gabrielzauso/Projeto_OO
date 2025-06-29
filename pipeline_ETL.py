class PipelineETL:
    def __init__(self):
        self.__etapas = []  # Encapsulamento

    def adicionar_etapa(self, etapa):
        self.__etapas.append(etapa)


    def executar(self, dados=None):  # Correção aqui
        for etapa in self.__etapas:
            dados = etapa.executar(dados)
        print("[PipelineTransformacao] Processo finalizado")
        return dados 