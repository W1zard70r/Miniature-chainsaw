tt='8'*86
while ('1111'in(tt) or '8888'in(tt)):
    if '1111'in(tt):
        tt = tt.replace('1111','8',1)
    else:
         tt = tt.replace('8888','11',1)
    print(tt)
