## стартовый модуль проекта

from functions import download_documents, process_documents
import os

def main():
   
    folder_url = 'https://drive.google.com/drive/folders/your-folder-id?usp=sharing'
    destination = 'documents'  
    
    
    if not os.path.exists(destination):
        print("Папка не существует, создаём...")
        download_documents(folder_url, destination)  
    else:
        print(f"Папка '{destination}' уже существует. Пропускаем скачивание.")
    
   
    process_documents(destination)  
    print("Обработка завершена!")

if __name__ == "__main__":
    main()
