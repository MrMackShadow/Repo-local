with open("text_6.txt", "w+", encoding="utf-8") as list_1:
    numbers = input('Введите цифры: ')
    list_1.writelines(numbers)

    print(sum(map(int, numbers.split())))