al='0123456789abcde'
for i in al:
    s=int(f'123{i}5',15) + int(f'1{i}233',15)
    if s%14==0:
        print(int(str(s//14),10))
