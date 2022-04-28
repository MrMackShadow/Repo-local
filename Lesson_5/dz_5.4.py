list_1 = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
list_2 = []
with open("Text_4.txt", "r", encoding="utf-8") as list_num:

    for i in list_num:
        i = i.split(' ', 1)
        print(i)
        list_2.append(list_1[i[0]] + '  ' + i[1])
    print(list_2)

with open('Text_5.txt', 'w', encoding="utf-8") as list_4:
    list_4.writelines(list_2)