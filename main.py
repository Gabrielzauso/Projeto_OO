from pipeline_ETL import PipelineETL
from extrator import ExtratorCSV,ExtratorAPI
from carregador import CarregadorCSV
from transformador import TransformadorMaiusculo, TransformadorRemoverEspacos

if __name__ == "__main__":
    pipeline = PipelineETL()

    pipeline.adicionar_etapa(ExtratorAPI("https://jsonplaceholder.typicode.com/users"))
    pipeline.adicionar_etapa(TransformadorRemoverEspacos("name"))
    pipeline.adicionar_etapa(TransformadorMaiusculo("name"))
    pipeline.adicionar_etapa(CarregadorCSV("usuarios.csv"))

    dados = pipeline.executar()
    print(dados)
