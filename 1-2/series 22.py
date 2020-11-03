n = int(input())
k=0
Flag = True
x = int(input())
for i in range(2, n+1):
    x1 = int(input())
    if Flag and (x1>x):
        Flag = False
        k = i
        x = x1
print(k)
    
