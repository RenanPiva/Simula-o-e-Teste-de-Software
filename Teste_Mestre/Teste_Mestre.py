import unittest
import xml.etree.ElementTree as ET
from parser import Parser, gerar_pdf

import PyPDF2


class CaseTests(unittest.TestCase):
  def ler_pdf(self, arquivo_pdf):
    """Lê o conteúdo de um PDF."""
    with open(arquivo_pdf, "rb") as f:
      reader = PyPDF2.PdfReader(f)
      texto = ""
      for page in reader.pages:
        texto += page.extract_text()
    return texto
  
  def test_MT_01(self):
    """
    Validar geração completa do PDF
    
    Entrada: XML com título, resumo, seções e referências
    Saida: PDF gerado corretamente com todos os elementos


    -- como comparar os dois pdf
    """
    
    arquivo_xml = "artigo.xml"
    arquivo_pdf = "artigo_formatado.pdf"
    arquivo_pdf_base = "artigo_formatado_base.pdf"
    dados = Parser(arquivo_xml).get_dados_completos()
    gerar_pdf(arquivo_pdf, dados)

    # Ler o PDF gerado e verificar seu conteúdo
    pdf_gerado = self.ler_pdf(arquivo_pdf)
    pdf_gerado_base = self.ler_pdf(arquivo_pdf_base)
    
    self.assertIn(pdf_gerado, pdf_gerado_base)

  def test_MT_02(self):
    """
    Testar fluxo de um XML corrompido
    
    Entrada: XML malformado
    Saida: Sistema identifica erro e retorna mensagem
    """
    
    arquivo_xml = "artigo_malformado.xml"
    arquivo_pdf = "artigo_formatado.pdf"

    with self.assertRaises(ET.ParseError) as context:
      dados = Parser(arquivo_xml).get_dados_completos()

    self.assertTrue('mismatched tag' in str(context.exception))

  def test_MT_03(self):
    """
    Testar processamento de um artigo sem referências
    
    Entrada: XML sem '<ref-list>'
    Saida: PDF gerado sem referências, sem erro
    """
    
    arquivo_xml = "artigo_sem_ref.xml"
    
    # with self.assertRaises(ET.ParseError) as context:
    dados = Parser(arquivo_xml).get_dados_completos()

    self.assertEqual(dados['referencias'], [])

  def test_MT_04(self):
    """
    Testar artigo com seção vazia
    
    Entrada: XML com '<sec>' sem 'p>'
    Saida: PDF gerado com título
    """
    
    arquivo_xml = "artigo_sem_sec.xml"
    
    dados = Parser(arquivo_xml).get_dados_completos()

    self.assertEqual(dados["secoes"], [('Introdução', []), ('Metodologia', []), ('Resultados', []), ('Conclusão', [])])

  def test_MT_05(self):
    """
    Testar um artigo sem autores
    
    Entrada: XML sem '<contrib-group>'
    Saida: PDF gerado sem erro, sem autores no cabeçalho
    """
    
    arquivo_xml = "artigo_sem_contrib.xml"
    
    dados = Parser(arquivo_xml).get_dados_completos()

    self.assertEqual(dados['autores'], [])

  def test_MT_06(self):
    """
    Testar integração com múltiplos arquivos
    
    Entrada: Múltiplos XMLs
    Saida: Todos os arquivos são processados sem erro
    """
    
    arquivos_xml = ["artigo.xml", "artigo_v1.xml", "artigo_v2.xml"]
    arquivo_pdf = "artigo_formatado.pdf"
    
    for arquivo_xml in arquivos_xml:
      dados = Parser(arquivo_xml).get_dados_completos()

      self.assertEqual(gerar_pdf(arquivo_pdf, dados), None)
    
if __name__ == '__main__':
  unittest.main(verbosity=1)