s = input("Введите строку: ") #ввод строки
k = 0 #счётчик для строк с подстрокой s
with open("text.txt", "r") as file: #открывается файл для чтения
    file_text = file.read().splitlines() #записывается текст, разбитый на строки
for string in file_text: #просматриваются строки
    if s in string: #если в строке есть подстрока, то она выводится на экран и к+1
        print(string)
        k += 1
print(f"Количество строк с подстрокой {s}: {k}") #вывод количества
print("Отсортированные по длине строки: ", sorted(file_text, key = len)) #вывод отсортированных по длине строк