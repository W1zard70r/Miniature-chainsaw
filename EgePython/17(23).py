with open('17.txt')as f:
    a=[int(x)for x in f]
    g=[x for x in a if x%10==3]
    g=max(g)
    cs=[]
    for x,y in zip(a,a[1:]):
        if (((abs(x)%10==3) and (abs(y)%10!=3)) or ((abs(y)%10==3) and (abs(x)%10!=3))) and (x**2+y**2>=g**2):
            cs.append(x**2+y**2)
    print(len(cs),max(cs))
            
