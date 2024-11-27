import os
from docx import Document

def update_document_format(file_path):
    """Изменяет формат документа: шрифт, размер шрифта и межстрочный интервал."""
    pass

def process_documents(source_folder):
    """Обрабатывает все документы .docx в папке."""
    for filename in os.listdir(source_folder):
        if filename.endswith(".docx"):  # Проверяем, что это файл .docx
            file_path = os.path.join(source_folder, filename)
            update_document_format(file_path)  # Важно: вызываем функцию, которая обновляет формат
        else:
            print(f"Файл {filename} не является .docx, пропускаем.")
