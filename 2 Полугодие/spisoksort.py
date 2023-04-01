a=[int(x) for x in input().split()]  # ввод списка
e=len(a)
Fl=False
while not(Fl):      # бесконечный цикл для сортировки списка с условием выхода
    for i in range(e):          # сравнение элемента со всеми элементами списка и замена
        f=a[i]
        for x in range(i,e):
            if f<=a[x]:
                continue
            else:
                a[i],a[x]=a[x],a[i]
    if all(a[i]<=a[i+1] for i in range(e-1)):   # проверка на верную сортировку
        Fl=True
print('end - ',a)   
