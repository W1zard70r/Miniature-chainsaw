a=[1,4,5,6,7,2,3,4,5,9,1289214,1,1,2,4,2,5,0]
e=len(a)
Fl=False
while not(Fl):
    for i in range(e):
        f=a[i]
        for x in range(i,e):
            if f<=a[x]:
                continue
            else:
                a[i],a[x]=a[x],a[i]
        
    print(a)
    if all(a[i]<=a[i+1] for i in range(e-1)):
        Fl=True
print('end - ',a)
