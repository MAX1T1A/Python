import easyocr


def text_recognition(file_path):
	reader = easyocr.Reader(['ru'])
	result = reader.readtext(file_path, detail=0, paragraph=True)

	return result


def main():
	file_path = input('Введите путь к файлу: ')
	print(text_recognition(file_path=file_path))


main()
