import os
import re
import opencc

def batch_convert():
    print("Initialize opencc...")
    try:
        converter = opencc.OpenCC('tw2s.json')
    except Exception as e:
        print(f"Failed to init opencc: {e}")
        return

    target_dir = 'easy-paper'
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        return

    processed = 0
    extensions = ('.md', '.txt', '.tex', '.json', '.yml', '.yaml')
    
    print(f"Scanning directory: {target_dir}")
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(extensions):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    orig_content = content
                    
                    # 1. OpenCC conversion
                    content = converter.convert(content)
                    
                    # 2. Case-insensitive regex replacement for "Traditional Chinese" -> "Simplified Chinese"
                    content = re.sub(r'(?i)traditional\s+chinese', 'Simplified Chinese', content)
                    
                    # 3. Direct replacement for "繁体中文" / "繁體中文"
                    content = content.replace('繁體中文', '简体中文').replace('繁体中文', '简体中文')
                    
                    if content != orig_content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        processed += 1
                        print(f"Updated: {path}")
                except Exception as e:
                    print(f"Error processing {path}: {e}")

    print(f"Conversion complete. Modified {processed} files.")

if __name__ == '__main__':
    batch_convert()
