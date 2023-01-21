tt=3*16**2018-2*8**1028-2**1050-3*4**1100-2022
s=[]
while tt!=0:
    s.append(str(tt%4))
    tt=tt//4

s=''.join(s)
print(s.count('3'))
