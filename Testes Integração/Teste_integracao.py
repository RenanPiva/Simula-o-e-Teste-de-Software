import xml.etree.ElementTree as ET
import unittest
from parser1 import Parser, gerar_pdf

class Teste(unittest.TestCase):
    # Sequência de testes

    # IT-01 Testar extração e formatação completa do artigo 👍
    def test_IT_01(self):
        print("\nIT-01:")
        arquivo_xml = "artigo.xml"
        arquivo_pdf = "artigo_formatado.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        assert dados == {'titulo': 'Uma Abordagem para Testes de Software Baseados em Inteligência Artificial', 'autores': ['João Silva', 'Maria Oliveira'], 'resumo': 'Este artigo apresenta uma abordagem inovadora para testes de software utilizando algoritmos de inteligência artificial. A metodologia proposta visa reduzir o tempo de execução dos testes e aumentar a cobertura dos cenários testados.', 'secoes': [('Introdução', ['Os testes de software são essenciais para garantir a qualidade dos sistemas modernos. Com o aumento da complexidade dos sistemas, métodos tradicionais de teste tornam-se ineficientes.']), ('Metodologia', ['Nossa metodologia propõe um modelo baseado em aprendizado de máquina para identificar falhas de software automaticamente.']), ('Resultados', ['Os testes realizados mostraram uma redução de 30% no tempo de execução e um aumento de 25% na detecção de falhas em comparação com abordagens tradicionais.']), ('Conclusão', ['Os resultados indicam que o uso de inteligência artificial em testes de software pode trazer benefícios significativos para a indústria.'])], 'referencias': ['Machine Learning in Software Testing, Journal of Software Engineering, 2022', 'Título desconhecido, Artificial Intelligence in Testing, 2021']}, "Deu bom"
        print(f"Passou no teste!\n{dados}")
        

    #IT-02 Testar pipeline de extração e geração de PDF 👍
    def test_IT_02(self):
        print("\nIT-02:")
        arquivo_xml = "artigo.xml"
        arquivo_pdf = "artigo_formatado.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado"
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # IT-03 Testar integração com XML sem título 👍
    def test_IT_03(self):
        print("\nIT-03:")
        arquivo_xml = "artigo_sTitulo.xml"
        arquivo_pdf = "artigo_formatado_sTitulo.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        # print(dados)
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # # Testar integração com XML sem autores 👍
    def test_IT_04(self):
        print("\nIT-04:")
        arquivo_xml = "artigo_sAutor.xml"
        arquivo_pdf = "artigo_formatado_sAutor.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        # print(dados)
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # # IT-05 Testar integração com XML sem resumo  👎
    def test_IT_05(self):
        print("\nIT-05:")
        arquivo_xml = "artigo_sResumo.xml"
        arquivo_pdf = "artigo_formatado_sResumo.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # # IT-06 Testar integração com XML contendo referências incompletas 👍
    def test_IT_06(self):
        print("\nIT-06:")
        arquivo_xml = "artigo_refsIncompleta.xml"
        arquivo_pdf = "artigo_formatado_refsIncompleta.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        # # print(dados)
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # # IT-07  Testar integração com XML contendo título longo 👍
    def test_IT_07(self):
        print("\nIT-07:")
        arquivo_xml = "artigo_tituloLongo.xml"
        arquivo_pdf = "artigo_formatado_tituloLongo.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        # print(dados)
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # # IT-08 Testar integração com XML contendo resumo longo 👍
    def test_IT_08(self):
        print("\nIT-08:")
        arquivo_xml = "artigo_resumoLongo.xml"
        arquivo_pdf = "artigo_formatado_resumoLongo.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        # print(dados)
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # # IT-09 Testar integração com múltiplos autores
    def test_IT_09(self):
        print("\nIT-09:")
        arquivo_xml = "artigo_multiAutor.xml"
        arquivo_pdf = "artigo_formatado_multiAutor.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        # print(dados)
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # # IT-10 Testar integração sem seções definidas 👍
    def test_IT_10(self):
        print("\nIT-10:")
        arquivo_xml = "artigo_semSec.xml"
        arquivo_pdf = "artigo_formatado_semSec.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        # print(dados)
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # # # IT-11  Testar fluxo de geração de PDF sem referências 👍
    def test_IT_11(self):
        print("\nIT-11:")
        arquivo_xml = "artigo_semRefs.xml"
        arquivo_pdf = "artigo_formatado_semRefs.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        # print(dados)
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

    # # IT-12   Testar fluxo completo com diversas variações do XML ?
    def test_IT_12(self):
        print("\nIT-12:")
        arquivo_xml = "artigo_variado.xml"
        arquivo_pdf = "artigo_formatado_variado.pdf"
        parser = Parser(arquivo_xml)
        dados = parser.get_dados_completos()
        # print(dados)
        assert gerar_pdf(arquivo_pdf, dados) == None, "Arquivo não gerado."
        print(f"PDF '{arquivo_pdf}' gerado com sucesso!")

print("Inicio de testes:\n")
Teste.test_IT_01(Teste)
Teste.test_IT_02(Teste)
Teste.test_IT_03(Teste)
Teste.test_IT_04(Teste)
Teste.test_IT_05(Teste)
Teste.test_IT_06(Teste)
Teste.test_IT_07(Teste)
Teste.test_IT_08(Teste)
Teste.test_IT_09(Teste)
Teste.test_IT_10(Teste)
Teste.test_IT_11(Teste)
Teste.test_IT_12(Teste)