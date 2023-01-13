a=bin(79)[2:]
for i in range(2):
    a=a+str((a.count('1')%2))
print(a)
