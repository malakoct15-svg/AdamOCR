import os
from paddleocr import PaddleOCR

# إعداد PaddleOCR للغة العربية
# نستخدم نسخة خفيفة عشان تخلص بسرعة
ocr = PaddleOCR(use_angle_cls=True, lang='ar', show_log=False)

input_dir = 'input_images'
output_file = 'result.txt'

all_text = []

if os.path.exists(input_dir):
    # ترتيب الصور أبجدياً (عشان لو الصفحة 1 و 2)
    files = sorted(os.listdir(input_dir))
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, file)
            result = ocr.ocr(img_path, cls=True)
            for idx in range(len(result)):
                res = result[idx]
                if res:
                    for line in res:
                        text = line[1][0]
                        all_text.append(text)

# حفظ النتيجة في ملف نصي
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_text))

print("✅ OCR Process completed. Output saved to result.txt")