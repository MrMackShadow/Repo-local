file = open("text_1.txt", "w", encoding="utf-8")
list_1 = 0
while True:
    if list_1 != "":

        list_1 = input('Введите слово, когда надоест просто нажмите "Enter" для выхода: ')
        file.writelines(list_1)
        file.writelines("\n")
    else:
        break
file.close()
