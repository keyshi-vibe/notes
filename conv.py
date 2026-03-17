import os
import re
import urllib.parse

# Регулярное выражение для поиска [[WikiLinks]]
pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'

def convert_links(content):
    def replace(match):
        filename = match.group(1).strip()
        # Кодируем пробелы и спецсимволы для URL (пробел станет %20)
        encoded_filename = urllib.parse.quote(filename)
        return f"[{filename}]({encoded_filename}.md)"
    
    return re.sub(pattern, replace, content)

def process_vault():
    # Скрипт работает в той папке, где запущен, и во всех вложенных
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                # Читаем файл
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        old_content = f.read()
                    except UnicodeDecodeError:
                        continue # Пропускаем бинарные файлы, если попадутся
                
                new_content = convert_links(old_content)
                
                # Если текст изменился, перезаписываем файл
                if old_content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"✅ Исправлено: {file_path}")

if __name__ == "__main__":
    print("🚀 Начинаю конвертацию ссылок для GitHub...")
    process_vault()
    print("✨ Готово! Все пробелы в ссылках заменены на %20.")