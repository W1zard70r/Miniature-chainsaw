from itertools import product
def f(x,y,z):
    count=0
    for l in range(2,z):
        b=product('12',repeat=l)
        b=list(b)
        for i in b:
            n=x
            if y>10 and i.count('2')>1:
                continue
            for a in range(len(i)):
                if n==17:
                    break
                if i[a]=='1':
                    n+=1
                elif i[a]=='2':
                    n=2
            if n==y:
                count+=1
    return(count)
print(f(1,10,10)f(10,35,25))
