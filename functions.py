
import os
from docx import Document

def update_document_format(file_path):
    """Изменяет формат документа: шрифт, размер шрифта и межстрочный интервал."""
    try:
        doc = Document(file_path)  # Открываем документ .docx  b
        print(f"Изменяем формат документа: {file_path}")
        
        # Изменение шрифта и размера шрифта
        for para in doc.paragraphs:
            for run in para.runs:
                run.font.name = 'Times New Roman'  # Меняем шрифт на Times New Roman
                run.font.size = 14  # Устанавливаем размер шрифта 14
            para.paragraph_format.line_spacing = 1.5  # Устанавливаем межстрочный интервал
        
        doc.save(file_path)  # Сохраняем документ с изменениями
        print(f"Документ {file_path} успешно сохранён с изменениями.")
    except Exception as e:
        print(f"Ошибка при обработке документа {file_path}: {e}")

def process_documents(source_folder):
    """Обрабатывает все документы .docx в папке."""
    pass
