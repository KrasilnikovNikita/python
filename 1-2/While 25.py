N = int(input())
f1=1
f2=1
f=f1+f2
while f<=N:
    f1=f2
    f2=f
    f=f1+f2
print(f)
