N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
maxx= 0
maxxi= 0
minx = 0
minxi = 0
minx = min(a)
minxi = a.index(min(a))
print(minx, minxi)


maxx = max(a)
for i in range(N):
    if a[i] >= maxx:
        maxx = a[i]
        maxxi = i
print(maxx,maxxi )
