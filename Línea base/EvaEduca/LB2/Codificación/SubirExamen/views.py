# SubirExamen/utils.py
import os # Proporciona funciones para interactuar con el sistema operativo y así manipular archivos y directorios
from docx import Document # Para manipular documentos word en python
from PyPDF2 import PdfReader # Para manipular documentos pdf en python

def leer_pdf(ruta_examen): 
    with open(ruta_examen, 'rb') as archivoPDF:
        leer = PdfReader(archivoPDF)
        texto = ""
        for pagina in leer.paginas:
            texto += pagina.extract_text().replace("\n", " ")
    return texto

def leer_docx(ruta_archivo):
    doc = Document(ruta_archivo)
    texto = ""
    for parrafo in doc.parrafos:
        texto += parrafo.text + "\n"
    return texto

