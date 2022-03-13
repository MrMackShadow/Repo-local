list = []
c = 4
p = 0
i = 0
# i задал количество значений в списке(так же через input можно попросить пользователя сделать это
while p < c:
    list.append(input('Введите любые данные: '))
    print(list)
    p += 1

for i in range(int(len(list)/2)):
    list[i], list[i + 1] = list[i + 1], list[i]
    i += 2
print(list)
