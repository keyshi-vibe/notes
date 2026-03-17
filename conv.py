import os
import re

pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'

def convert_links(content):
    return re.sub(pattern, r'[\1](\1.md)', content)

def process_files():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    old_content = f.read()
                
                new_content = convert_links(old_content)
                
                if old_content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Исправлено: {file_path}")

if __name__ == "__main__":
    process_files()
    print("ссылки стали стандартными.")