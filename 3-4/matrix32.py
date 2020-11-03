M = int(input())
N = int(input())
a = []
p = 0
o = 0
stroka = 0
MAT = []
for i in range(N):
    a.append(int(input()))
    
for i in range(M):
    MAT.append(a)

b = []
for i in range(N):
    b.append(int(input()))

for i in range(4,5):
    MAT[i] = b

for i in range(M):
    print(MAT[i])

for i in range(M):
    for j in range(N):
        if MAT[i][j]>=0:
            p=p+1
        else:
            o=o+1
    if p==o:
     stroka = i
     break
    p = 0
    o = 0
if stroka == 0:
    print(0)
else:
    print(stroka)
