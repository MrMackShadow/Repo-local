with open("Text_3 Name and salary.txt", "r", encoding="utf-8") as text_3:
    salary = []
    Losers = []
    list_1 = text_3.read().split('\n')
    for i in list_1:
        i = i.split()

        if float(i[1]) < 20000.00:
            Losers.append(i[0])
        salary.append(i[1])

print(f'Люди с окладом меньше 20000.00: {Losers}, \nСредний оклад: {sum(map(float, salary)) / len(salary)}')
