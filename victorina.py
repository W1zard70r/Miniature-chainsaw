a = ["какой сейчас год?", "самый старый учитель ЛТПУ?", 'Веришь в бога?',
     'айтишник ли ты?', 'Сколько углов в треугольнике?']
scores = int(0)
for i in range(len(a)):
    if i == 0:
        answer = int(input(f'{a[i]}\n'))
        if answer == 2022:
            scores += 1
    if i == 1:
        answer = int(input(f'{a[i]}\n   1 - Лариса Хазиевна Казанцева\n   2 - Ольга Владимировна\n   3 - Семен Даньшин\n   4 - Надежда Усова\n'))
        if answer == 1:
            scores += 1
    if i == 2:
        answer = input(f'{a[i]}\n')
        if answer == 'да':
            scores += 1
    if i == 3:
        answer = input(f'{a[i]}\n')
        if answer == 'да':
            scores += 1
    if i ==4:
        answer = int(input(f'{a[i]}\n'))
        if answer == 3:
            scores += 1
print(f'оценка тебя - {scores}')