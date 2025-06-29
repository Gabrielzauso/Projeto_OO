class PipelineETL:
    def __init__(self):
        self.__etapas = []  # Encapsulamento

    def adicionar_etapa(self, etapa):
        self.__etapas.append(etapa)


    def executar(self, dados=None):  # Correção aqui
        for etapa in self.__etapas:
            try:
                    dados = etapa.executar(dados)
                    print(f"[{etapa.__class__.__name__}] Processo finalizado")
                
            except Exception as e:
                 print(f"[ERRO] Falha na etapa {etapa.__class__.__name__}: {e}")
                 print("[PipelineETL] Execução interrompida devido ao erro.")
                 break  # Para o pipeline aqui
        
        return dados