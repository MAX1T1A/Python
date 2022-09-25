import cv2
import pytesseract

# Путь для подключения tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Путь картинки
file_path = input('File path: ')

# Подключение фото
img = cv2.imread(file_path)

# Выбор языка
language = input('Language(rus, eng): ').lower()

# Будет выведен весь текст с картинки
image_text = pytesseract.image_to_string(img, config=r'--oem 3 --psm 6', lang=language)
print(f'\n{image_text}\n')

# Запсись текста в текстовый файл
file_text = open ('photo_text.txt', 'a+', encoding='utf-8')
file_text.write(f'{image_text}\n---------------\n\n')