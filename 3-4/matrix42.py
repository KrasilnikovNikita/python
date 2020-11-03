M = int(input())
N = int(input())
a = []
k = 0
count = 0
MAT = []
for i in range(M):
    a.append(int(input()))

    
for i in range(N):
    MAT.append(a)

#for i in range(N):
#    print(MAT[i])

b = []
for i in range(M):
    b.append(int(input()))

c = []
for i in range(M):
    c.append(int(input()))

for i in range(1,2):
    MAT[i] = b

for i in range(4,5):
    MAT[i] = c

for i in range(M):
    for j in range(N-1):
        if MAT[i][j]<MAT[i][j+1]:
            k=k+1
    if k==N-1:
        count=count+1
    k=0
for i in range(N):
    print(MAT[i])
print(count)
    
    
