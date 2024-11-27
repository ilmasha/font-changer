import os
import requests
import zipfile
from docx import Document

def download_file_from_google_drive(file_id, destination):
    """Скачивает файл с Google Drive и проверяет его корректность"""
    URL = f"https://drive.google.com/uc?export=download&id={file_id}"
    session = requests.Session()
    response = session.get(URL, stream=True)
    
    # Проверка, что скачанный файл не пустой
    if response.status_code != 200:
        print(f"Ошибка скачивания файла {file_id}. Код ответа: {response.status_code}")
        return False
    
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(1024):
            if chunk:
                f.write(chunk)

    # Проверка, что файл является настоящим .docx (ZIP-архив)
    if not zipfile.is_zipfile(destination):
        print(f"Файл {destination} не является валидным .docx файлом.")
        os.remove(destination)  # Удаляем повреждённый файл
        return False

    print(f"Файл {destination} скачан и проверен как .docx!")
    return True

def download_documents(folder_url, destination):
    """Скачивает все файлы из указанной папки Google Drive"""
    # Пример списка ID файлов (замените на свои реальные ID файлов)
    file_ids = [
        "1HcQjoxdNdJrQlVqWk5v3fnP5exO7d3oG",  # Пример ID
        "1LQJvFzOS0tW7-TfAzw7L4VpS0EEXAMPLE"   # Пример ID другого файла
    ]
    
    for file_id in file_ids:
        # Указываем путь для скачивания
        file_path = os.path.join(destination, f"{file_id}.docx")
        
        # Скачиваем файл и проверяем, что он корректно скачан
        if download_file_from_google_drive(file_id, file_path):
            print(f"Файл {file_id}.docx успешно скачан и готов к обработке!")
        else:
            print(f"Ошибка при скачивании файла {file_id}.docx.")

def process_documents(destination):
    """Обрабатывает все скачанные документы"""
    for filename in os.listdir(destination):
        if filename.endswith('.docx'):
            file_path = os.path.join(destination, filename)
            update_document_format(file_path)

