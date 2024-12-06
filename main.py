"""Написать программу, которая:
- Запрашивает у пользователя строку для поиска.
- Находит и выводит все строки, которые содержат искомую подстроку, а также их количество из следующего файла.
- Сортирует найденные строки в порядке их длины (от самой короткой к самой длинной) и выводит их."""

searchStr = input("Введите искомую строку: ") #Ввод искомой строки с клавиатуры
with open('text.txt', 'r', encoding = "Windows 1251") as text: #Открытие файла для чтения с помощью кодировки Windows 1251 и присваивание файла переменной text
    lines=text.readlines() #Чтение файла построчно

listOfStr = [] #Создание пустого списка для строк с искомой подстрокой
for line in lines: #Цикл for для перебора строк текста
    if searchStr in line: #Цикл if для проверки наличия искомой подстроки в строке
        listOfStr.append(line.strip()) #Добавление строки в список при истинности условия
strLength = len(listOfStr) #Создание переменной подсчитывающей кол-во строк с искомой подстрокой
print("Кол-во строк с искомой подстрокой: ", strLength) #Вывод текста на консоль

for line in sorted(listOfStr, key = len): #Цикл for для перебора строк в отсортированном по длине списке
    print(line) #Вывод строки на консоль