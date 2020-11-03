N = int(input())
K = int(input())
S = 0
X = 1
for i in range(0, N+1):
    if X!=N:
     S = S + X**K
     X = X + 1
S = S + N**K
print(S)
