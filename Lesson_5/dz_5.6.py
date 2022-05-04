dict_1 = {}
with open("text_7.txt", "r", encoding="utf-8") as file:
    list_1 = file.read().split("\n")[:-1]

for item in list_1:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict_1[key] = value

print("Сумма всех часов: ")

list_2 = lambda x: int('0' + ''.join([e for e in x if e.isdigit()]))
for k, v in dict_1.items():
    print(f'{k}={sum([list_2(e) for e in v])}')
