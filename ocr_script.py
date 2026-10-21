import os
from paddleocr import PaddleOCR

# إعداد PaddleOCR للغة العربية (متوافق مع الإصدارين 2 و 3)
ocr = PaddleOCR(use_angle_cls=True, lang='ar')

input_dir = 'input_images'
output_file = 'result.txt'

all_text = []

if os.path.exists(input_dir):
    # ترتيب الصور أبجدياً
    files = sorted(os.listdir(input_dir))
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, file)
            result = ocr.ocr(img_path)
            
            # التحقق من النتيجة (سواء كانت إصدار قديم أو جديد)
            if not result or result[0] is None:
                continue
                
            # الإصدار القديم v2 (يرجع list of lists)
            if isinstance(result[0], list):
                for line in result[0]:
                    all_text.append(line[1][0])
            # الإصدار الجديد v3 (يرجع list of dicts)
            elif isinstance(result[0], dict) and 'rec_texts' in result[0]:
                all_text.extend(result[0]['rec_texts'])
            elif hasattr(result[0], 'get') and 'rec_texts' in result[0]:
                all_text.extend(result[0]['rec_texts'])

# حفظ النتيجة في ملف نصي
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_text))

print("✅ OCR Process completed. Output saved to result.txt")