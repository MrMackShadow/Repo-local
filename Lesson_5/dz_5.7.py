import json

# Создал файл с латинницей чтобы json был выглядел привлекательнее.

profit = {}
prof = 0
average_profit = 0
i = 0
with open('firms.txt', 'r', encoding="utf-8") as firms:

    for line in firms:
        firm, type_f, earning, damage = line.split()
        profit[firm] = int(earning) - int(damage)
        if profit.setdefault(firm) >= 0:
            prof = prof + profit.setdefault(firm)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Average profit - {average_profit:.2f}')
    else:
        print(f'Average profit - Non')
    end_list = {'Average profit': round(average_profit)}
    profit.update(end_list)
    print(f'Profit all company - {profit}')

with open('firms.json', 'w', encoding="utf-8") as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)