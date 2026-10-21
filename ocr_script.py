import os
import pytesseract
from PIL import Image

input_dir = 'input_images'
output_file = 'result.txt'
all_text = []

if os.path.exists(input_dir):
    files = sorted(os.listdir(input_dir))
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, file)
            try:
                img = Image.open(img_path)
                text = pytesseract.image_to_string(img, lang='ara+eng')
                if text.strip():
                    all_text.append(text.strip())
            except Exception as e:
                print(f"Error processing {file}: {e}")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_text))

print("✅ OCR Process completed. Output saved to result.txt")