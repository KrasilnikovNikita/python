N =int(input())
a = []
s=0
for i in range (N):
    a.append(float(input()))
for i in range(N):
    a[i]=int(a[i])
    s=s+a[i]
print(a)
print(s)
    
