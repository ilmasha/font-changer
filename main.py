import os
from functions import process_documents  # Импортируем функцию для обработки документов

def main():
    # Папка, где находятся файлы .docx
    source_folder = 'documents'

    # Проверяем, существует ли папка с документами
    if not os.path.exists(source_folder):
        print(f"Папка {source_folder} не существует. Создаём её...")
        os.makedirs(source_folder)
    else:
        print(f"Папка {source_folder} найдена.")

    # Вызываем функцию для обработки документов в указанной папке
    process_documents(source_folder)

# Запуск скрипта
if __name__ == "__main__":
    main()
