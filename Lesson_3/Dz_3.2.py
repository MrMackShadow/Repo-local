def fun_2(**kwargs):
    return kwargs
print(fun_2(first_name=input("Введите ваше имя: "),
            last_name=input("Введите вашу фамилию: "),
            year_bith=int(input("Введите ваш год рождения: ")),
            city=input("Введите ваш город: "),
            email=input("Введите вашу почту: "),
            phone=int(input("Введите ваш телефон: "))))

print(fun_2())
