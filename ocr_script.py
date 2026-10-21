import os
from paddleocr import PaddleOCR

# إعداد PaddleOCR للغة العربية
# تم إزالة show_log و use_angle_cls لأنها بترمي خطأ في النسخ الجديدة
ocr = PaddleOCR(lang='ar')

input_dir = 'input_images'
output_file = 'result.txt'
all_text = []

if os.path.exists(input_dir):
    # ترتيب الصور أبجدياً (عشان لو الصفحة 1 و 2)
    files = sorted(os.listdir(input_dir))
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, file)
            
            try:
                result = ocr.ocr(img_path)
                
                if not result or result[0] is None:
                    continue
                
                # التعامل مع الإصدار الجديد v3 (بيرجع dict فيها rec_texts)
                if isinstance(result[0], dict) or hasattr(result[0], 'get'):
                    for res in result:
                        if 'rec_texts' in res:
                            all_text.extend(res['rec_texts'])
                            
                # التعامل مع الإصدار القديم v2 (بيرجع list of lists)
                elif isinstance(result[0], list):
                    for line in result[0]:
                        if line and len(line) > 1:
                            all_text.append(line[1][0])
                            
            except Exception as e:
                print(f"Error processing {file}: {e}")

# حفظ النتيجة في ملف نصي
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_text))

print("✅ OCR Process completed. Output saved to result.txt")
