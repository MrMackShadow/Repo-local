user_answer = input('Введите любое предложение: ')
list = user_answer.split()

for ind, el in enumerate(list, 1):
    print(ind, el)
