N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
n = 0
e = 0
k = 0
maxx = 0
poz = 0
for i in range(N):
    if i == 0:
        if a[i] == 0:
            fl = False
            n = n+1
            poz = i
        else:
            fl = True
            e = e+1
            poz = i
    
    if i > 0:
        if a[i] == 0:
            if fl == True:
                fl = False
                if maxx < e:
                    maxx = e
                    poz = i - maxx
                e = 0
            n = n + 1
        else:
            if fl == False:
                fl = True
                if maxx < n:
                    maxx = n
                    poz = i - maxx
                n = 0
            e = e + 1
print(poz, maxx)
