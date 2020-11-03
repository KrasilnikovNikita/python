N = int(input())
a = []
b = []
for i in range(N):
    a.append(int(input()))
for i in range(0,N,2):
    b.append(a[i])
for i in range(1,N,2):
    b.append(a[i])
print(b)


    
