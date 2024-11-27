## стартовый модуль проекта

import os
from functions import download_documents, process_documents

def main():
    destination_folder = 'documents'

    if not os.path.exists(destination_folder):
        print("Папка не существует, создаём...")
        os.makedirs(destination_folder)
    
    # Скачиваем документы с Google Drive и проверяем их
    file_ids = [
        "1HcQjoxdNdJrQlVqWk5v3fnP5exO7d3oG",  
        "1LQJvFzOS0tW7-TfAzw7L4VpS0EEXAMPLE"   
    ]
    
    for file_id in file_ids:
        file_path = os.path.join(destination_folder, f"{file_id}.docx")
        if download_documents(file_id, file_path):
            print(f"Файл {file_id}.docx успешно скачан и готов к обработке!")
        else:
            print(f"Ошибка при скачивании файла {file_id}.docx.")

    # Обрабатываем все скачанные документы
    process_documents(destination_folder)

if __name__ == "__main__":
    main()
