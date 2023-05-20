f=open('24-241.txt','r')
f=f.readline().split('E')
coun=[]
for i in range(len(f)):
    if f[i].count('A')>5 and f[i].count('B')==2:
        t=0
        y=0
        for b in range(len(f[i])):
            if f[i][b]=='B':
                t+=1
            if f[i][b]=='A' and t==1:
                y+=1
        if y>5:
            coun.append(2+len(f[i]))
print(min(coun))