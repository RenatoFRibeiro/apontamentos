
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
import os

# Pasta onde os arquivos XML estão localizados
xml_folder = 'fusrodah/'

# Pasta onde os arquivos PDF serão salvos
pdf_folder = 'fusrodah/pdfs'

# Estilos para o texto no PDF
styles = getSampleStyleSheet()
style_normal = styles['Normal']

# Percorre todos os arquivos na pasta de XMLs
for xml_file in os.listdir(xml_folder):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(xml_folder, xml_file)
        pdf_path = os.path.join(pdf_folder, xml_file.replace('.xml', '.pdf'))

        # Abre e lê o conteúdo do arquivo XML (você precisará de uma biblioteca XML para isso)
        with open(xml_path, 'r') as xml_content:
            xml_data = xml_content.read()

        # Cria um documento PDF
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)

        # Converte o conteúdo XML em um parágrafo para o PDF
        para = Paragraph(xml_data, style_normal)

        # Adiciona o parágrafo ao documento PDF
        doc.build([para])

print("Conversão concluída!")
