N = int(input())
a = []
b = []
c = []
for i in range(N):
    a.append(int(input()))
for i in range(N):
    b.append(int(input()))
for i in range(N):
    c.append(b[i])
b = []
for i in range(N):
    b.append(a[i])
a = []
for i in range(N):
    a.append(c[i])
print(a)
print(b)
