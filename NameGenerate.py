import random
def name():
    a= list(input('ваше имя: '))
    p = int(input('Укажите ваш пол(1 = женский, 2 = мужской): '))
    wends=['лини','али','ит','ин','ен','ис','ан','т','ик','ли']
    mends=['тини','кини','гек','бек','рек','пер','тор','мар']
    Sogl=['К','Н','Г','З','Х','В','П','Р','Л','Д','С','М','Т','Б','к','н','г','з','х','в','п','л','д','с','м','т','б']
    gl = ['а','е','и','ё','у','ы','о','э','я','ю','Ё','Е','У','О','Ы','А','Э','Я','И', 'Ю']
    ok = ['а','я']
    ngl=[]
    for i in range(len(a)):
        for b in range(len(gl)):
            if a[i]==gl[b]:
                ngl.append(a[i])
    word=[]
    b=''
    for i in range(len(ngl)):
        word.append(random.choice(Sogl))
        word.append(ngl[i])
    
    for i in range(len(word)):
        if i==0:
            b+=word[i].upper()
        elif i !=0:
            b+=word[i].lower()
    if p == 2:
        b+=random.choice(mends)
    if p == 1:
        b+=random.choice(wends)
        b+=random.choice(ok)
    print('Ваше имя - ', b)
def foo():
    n = True
    while n:
        arg = int(input('1 - сделать действие, 2 - показать список разработчиков'))
        if arg == 1:
            name()
        else:
            print('''        Силков Александр Максимович - 1 Разработчик
            Степанов Михаил Сергеевич - 2 Разработчик
            Семенов Алексей Павлович - тестировщик
            Эков Илья Андреевич - Искатель Альтернатив
            Скачкаускас Матвей Александрович - помощник 2 разрабочика
            Хузеев Кирилл Юрьевич - глваный тестировщик
            ''')
        new = int(input('запустить программу еще раз?(1 - да, 2 - нет)'))
        if new == 1:
            n = True
        else:
            n = False
            print('ок, до свидания')
if __name__ == '__main__':
    foo()
