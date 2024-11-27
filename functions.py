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


def func2(n):
    """Функция 2"""


def func3(n):
    """Функция 3"""
    pass