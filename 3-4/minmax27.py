N = int(input())
a = []
k = 0
c = 0
m = 0
poz = 0
maxi = 0
for i in range(0, N):
    a.append(int(input()))
    
for i in range(0, N):
    if k == 0:
        m=a[i]
        k = 1
        poz = i
    if a[i] ==m:
        c += 1
        k = 1
        
    elif c > maxi:
        n=poz
        maxi = c
        c = 0
        k = 0
    elif c < maxi:
        c = 0
        k = 0

if c > maxi:
    maxi = c
        
if maxi != 0:
    print(n, maxi)

