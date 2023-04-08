word='миа'
alf=['м','и','а']
m=['***    ***','** **** **','**  **  **','**      **','**      **']
u=['**     ***','**    ****','**   ** **','*****   **','***     **']
a=['    **    ','   ****   ','  **  **  ',' ******** ','***    ***']
mat=[m,u,a]
ch=[alf.index(x) for x in list(word)] 
for i in range(len(mat[0])):
    for g in range(len(ch)):
        print(mat[ch[g]][i],end=' ')
    print()


