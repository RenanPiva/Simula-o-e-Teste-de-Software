import unittest
from parser import Parser

class CaseTests(unittest.TestCase):
  
  # Testes de unidade
  #Verificar extração do título
  def test_UT_01(self):
    """
    Verificar extração do título
    
    Entrada: XML válido
    Saida: Retorna título do artigo
    """
    arquivo_xml = "artigo.xml"

    self.assertEqual(Parser(arquivo_xml).get_titulo(), 'Uma Abordagem para Testes de Software Baseados em Inteligência Artificial')

  #Verificar extração de autores
  def test_UT_02(self):
    """ Verificar extração de autores
    
    Entrada: XML válido
    Saida: Retorna lista de autores
    """
    
    arquivo_xml = "artigo.xml"

    self.assertEqual(Parser(arquivo_xml).get_autores(), ['João Silva', 'Maria Oliveira'])

  #Testar resumo do artigo
  def test_UT_03(self):
    """
    Testar resumo do artigo
    
    Entrada: XML válido
    Saida: Retorna o resumo do artigo
    """
    
    arquivo_xml = "artigo.xml"

    self.assertEqual(Parser(arquivo_xml).get_resumo(), 'Este artigo apresenta uma abordagem inovadora para testes de software utilizando algoritmos de inteligência artificial. A metodologia proposta visa reduzir o tempo de execução dos testes e aumentar a cobertura dos cenários testados.')

  #Validar extração de seções
  def test_UT_04(self):
    """ 
    Validar extração de seções
    """
    arquivo_xml = "artigo.xml"
    
    self.assertEqual(Parser(arquivo_xml).get_secoes(), [ (
            "Introdução",
            ["Os testes de software são essenciais para garantir a qualidade dos sistemas modernos. Com o aumento da complexidade dos sistemas, métodos tradicionais de teste tornam-se ineficientes."]
        ),(
            "Metodologia",
            ["Nossa metodologia propõe um modelo baseado em aprendizado de máquina para identificar falhas de software automaticamente."]
        ),

        (
            "Resultados",
            ["Os testes realizados mostraram uma redução de 30% no tempo de execução e um aumento de 25% na detecção de falhas em comparação com abordagens tradicionais."]
        ),

        (
            "Conclusão",
            ["Os resultados indicam que o uso de inteligência artificial em testes de software pode trazer benefícios significativos para a indústria."]
    )])
    
    
  #Validar extração de referências
  def test_UT_05(self):
    """ 
    Validar extração de referências
    """
    arquivo_xml = "artigo.xml"
    
    # <source>Artificial Intelligence in Testing</source>
    # <year>2021</year>
    
    self.assertEqual(Parser(arquivo_xml).get_referencias(), ['Machine Learning in Software Testing, Journal of Software Engineering, 2022', 'Título desconhecido, Artificial Intelligence in Testing, 2021'])
    
  #Testar comportamento com XML inválido
  def test_UT_06(self):
    """ 
    Testar comportamento com XML inválido
    """
    
    arquivo_xml = "artigo_com_xml_invalido.xml"
    
    self.assertEqual(Parser(arquivo_xml).get_resumo(), None)
    
  #Testar a extração sem título
  def test_UT_07(self):
    """ 
    Testar a extração sem título
    """
    
    arquivo_xml = "artigo_sem_titulo.xml"
    
    self.assertEqual(Parser(arquivo_xml).get_titulo(), None)
    
    
  #Testar a extração sem autores
  def test_UT_08(self):
    """ 
    Testar a extração sem autoresS
    """
    
    arquivo_xml = "artigo_sem_autores.xml"
    
    self.assertEqual(Parser(arquivo_xml).get_autores(), ['None None', 'None None'])

  #testar referencias imcompletas
  def test_UT_09(self):
    """ 
    Testar referencias imcompletas
    """
    
    arquivo_xml = "artigo_referencias_imcompletas.xml"
    
    self.assertEqual(Parser(arquivo_xml).get_referencias(), ['Título desconhecido, Journal of Software Engineering, 2022', 'Título desconhecido, Artificial Intelligence in Testing, None'])
    
  #Testar titulo longo
  def test_UT_10(self):
    """ 
    Testar titulo longo
    """
    
    arquivo_xml = "artigo.xml"
    
    self.assertEqual(Parser(arquivo_xml).get_titulo(), 'Uma Abordagem para Testes de Software Baseados em Inteligência Artificial')

  #Testar resumo e seções vazias
  def test_UT_11(self):
    """ 
    Testar resumo e seções vazias
    """
    arquivo_xml = "artigo_resumo_vazio_e_secoes.xml"
    
    self.assertEqual(Parser(arquivo_xml).get_resumo(), None)
    self.assertEqual(Parser(arquivo_xml).get_secoes(), [(None, [None]), (None, [None]), (None, [None]), (None, [None])])

  #Testar resumo longo
  def test_UT_12(self):
    """ 
    Testar resumo longo
    """

    arquivo_xml = "artigo.xml"
    
    self.assertEqual(Parser(arquivo_xml).get_resumo(), 'Este artigo apresenta uma abordagem inovadora para testes de software utilizando algoritmos de inteligência artificial. A metodologia proposta visa reduzir o tempo de execução dos testes e aumentar a cobertura dos cenários testados.')

if __name__ == '__main__':
  unittest.main(verbosity=2)