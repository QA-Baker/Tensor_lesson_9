# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
import re

# Открытие исходного файла для чтения
with open("test_file/task1_data.txt", 'r', encoding='utf-8') as infile:
    # Чтение всего текста из файла
    text = infile.read()

    # Использование регулярного выражения для удаления всех цифр
    cleaned_text = re.sub(r'\d', '', text)

# Открытие файла для записи очищенного текста
with open("test_file/task1_answer.txt", 'w', encoding='utf-8') as outfile:
    # Запись очищенного текста в новый файл
    outfile.write(cleaned_text)
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
