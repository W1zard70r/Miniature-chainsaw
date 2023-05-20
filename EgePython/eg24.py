f=open('24-241.txt','r')
f=f.readline()
coun=[]
while f.count('E')>1:
    l=f.index('E')
    f=f.replace('E','*',1)
    p=f.index('E')
    f=f.replace('E','*',1)
    a=f[l+1:p]
    if a.count('B')==2:
        lb=a.index('B')
        a.replace('B','*',1)
        rb=a.index('B')
        a.replace('B','*',1)
        if a.count('A')>5:
            coun.append(2+p-l)
    f.replace('B','*',a.count('B'))
print(min(coun))