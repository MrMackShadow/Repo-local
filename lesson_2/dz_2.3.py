sesson_1 = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
sesson_2 = ['Зима', 'Весна', 'Лето', 'Осень']
user_answer = int(input('Пожалуйста введите номер месяца: '))
if user_answer == 12 or user_answer == 1 or user_answer == 2:
    print(sesson_1.get(1))
    print(sesson_2[0])
elif 3 <= user_answer <= 5:
    print(sesson_1.get(2))
    print(sesson_2[1])
elif 6 <= user_answer <= 8:
    print(sesson_1.get(3))
    print(sesson_2[2])
elif 9 <= user_answer <= 11:
    print(sesson_1.get(4))
    print(sesson_2[3])
else:
    print('Неккоректное значение')