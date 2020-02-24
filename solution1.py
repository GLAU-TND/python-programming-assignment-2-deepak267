f=eval(input())
b=[min(f)]
a=min(f)[-1]
f.remove(min(f))
for i in f:
    for j in f:
        if a==j[0] and j[-1]!=b[0][0]:
            b.append(j)
            a=j[-1]
            f.remove(j)
            break
b=b+f
print(b)
