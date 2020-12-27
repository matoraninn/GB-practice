import json
profit = {}
average = {}
x = 0
y = 0
i = 0
with open('practice_5.txt', 'r') as textfile:
    for line in textfile:
        name, firm, income, expenses = line.split()
        profit[name] = int(income) - int(expenses)
        if profit.setdefault(name) >= 0:
            x = x + profit.setdefault(name)
            i += 1
    if i != 0:
        y = x / i
        print(f'Средняя:{y:.2f}')
    else:
        print(f'Ошибка')
    x = {'Средняя': round(y)}
    profit.update(x)
    print(f'Прибыль каждой компании - {profit}')


with open('practice_j1.json', 'w') as js:
    json.dump(profit, js)

    jstext = json.dumps(profit)
    print(f'json фаил: \n 'f' {jstext}')