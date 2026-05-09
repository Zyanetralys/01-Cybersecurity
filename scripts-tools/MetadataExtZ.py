#!/usr/bin/env python3
import os
import sys
import argparse
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import PyPDF2
import docx

# ---------------------------
# EXTRACCIÓN DE METADATOS
# ---------------------------

def extract_image_metadata(filepath):
    try:
        image = Image.open(filepath)
        info = image._getexif()
        if info:
            print("\n[+] Metadatos de imagen:")
            for tag, value in info.items():
                tagname = TAGS.get(tag, tag)
                print(f"   {tagname}: {value}")
        else:
            print("   Sin metadatos EXIF detectados.")
    except Exception as e:
        print(f"   [!] Error analizando imagen: {e}")

def extract_pdf_metadata(filepath):
    try:
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            info = reader.metadata
            print("\n[+] Metadatos de PDF:")
            if info:
                for key, value in info.items():
                    print(f"   {key}: {value}")
            else:
                print("   No se encontraron metadatos.")
    except Exception as e:
        print(f"   [!] Error analizando PDF: {e}")

def extract_docx_metadata(filepath):
    try:
        doc = docx.Document(filepath)
        core_props = doc.core_properties
        print("\n[+] Metadatos de DOCX:")
        for attr in ["author", "title", "subject", "keywords", "created", "last_modified_by"]:
            val = getattr(core_props, attr)
            if val:
                print(f"   {attr}: {val}")
    except Exception as e:
        print(f"   [!] Error analizando DOCX: {e}")

def analyze_file(filepath):
    ext = os.path.splitext(filepath.lower())[1]
    print(f"\n[ * ] Analizando {filepath}")
    if ext in ['.jpg', '.jpeg', '.png']:
        extract_image_metadata(filepath)
    elif ext == '.pdf':
        extract_pdf_metadata(filepath)
    elif ext == '.docx':
        extract_docx_metadata(filepath)
    else:
        print("   [!] Tipo de archivo no soportado.")

# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zya Recon - Metadata Extractor")
    parser.add_argument("files", nargs='+', help="Lista de archivos a analizar")
    args = parser.parse_args()

    print(f"\n[ * ] Iniciando extracción de metadatos")
    print(f"[ * ] Hora de inicio: {datetime.now()}")
    for file in args.files:
        if os.path.isfile(file):
            analyze_file(file)
        else:
            print(f"\n[!] Archivo no encontrado: {file}")
    print("\n[ * ] Análisis finalizado.")
