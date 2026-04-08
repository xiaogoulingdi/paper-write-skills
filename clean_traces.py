import os
import re

def clean_residual_traces():
    target_dir = 'easy-paper'
    
    replacements = [
        (r'(?i)zh-tw', 'zh-CN'),
        (r'(?i)zh_tw', 'zh_CN'),
        (r'(?i)Taiwan(\'s)?', 'China'),
        (r'(?i)Taiwanese', 'Chinese'),
        (r'(?i)Taiwan National Digital Library of Theses and Dissertations', 'CNKI (China National Knowledge Infrastructure)'),
        (r'(?i)Airiti Library', 'Wanfang Data')
    ]
    
    processed = 0

    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(('.md', '.txt', '.tex', '.json', '.yml', '.yaml')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    orig_content = content
                    
                    for old, new in replacements:
                        content = re.sub(old, new, content)
                    
                    if content != orig_content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        processed += 1
                        print(f"Cleaned traces in: {path}")
                except Exception as e:
                    print(f"Error cleaning {path}: {e}")
                    
    print(f"\nDone. Cleaned {processed} files.")

if __name__ == '__main__':
    clean_residual_traces()
