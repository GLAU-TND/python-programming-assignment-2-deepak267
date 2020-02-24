v=eval(input())
v=[str(i) for i in v]
v.sort()
b=''
for i in range(len(v)-1):
    if v[i][0]==v[i+1][0] and len(v[i])<len(v[i+1]):
        a=v[i]
        v[i]=v[i+1]
        v[i+1]=a
for i in range(len(v)-1,-1,-1):
    b=b+v[i]
print(int(b))
