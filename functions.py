## functions модуль для импорта функций для работы

import os
import requests
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.enum.text import WD_LINE_SPACING

def download_file_from_google_drive(file_id, destination):
    """Скачивает файл с Google Drive по ID"""
    URL = f"https://drive.google.com/uc?export=download&id={file_id}"
    session = requests.Session()
    response = session.get(URL, stream=True)
    
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(1024):
            if chunk:
                f.write(chunk)
    print(f"Файл {destination} скачан!")


def download_documents(folder_url, destination):
    """Скачивает все файлы из папки Google Drive"""
    
    file_ids = [
        "1HcQjoxdNdJrQlVqWk5v3fnP5exO7d3oG",  
        "1LQJvFzOS0tW7-TfAzw7L4VpS0EEXAMPLE"
    ]
    
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for file_id in file_ids:
        file_name = f"{file_id}.docx"
        file_path = os.path.join(destination, file_name)
        download_file_from_google_drive(file_id, file_path)


def update_document_format(file_path):
    """Изменяет шрифт, размер и межстрочный интервал в документе"""
    doc = Document(file_path)
    
    for para in doc.paragraphs:
        for run in para.runs:
            run.font.name = 'Times New Roman'  # Установка шрифта
            run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')  # Поддержка шрифта для всех языков
            run.font.size = Pt(14)  # Установка размера шрифта
        
        # Установка межстрочного интервала 1.5
        para.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE  # Межстрочный интервал 1.5
        doc.save(file_path)  # Сохранение изменени
    pass