x1= 0
x2 = 1
x3 = 2
k = 2
E = int(input())
while E<abs(x3-x2):
    x1=x2
    x2=x3
    x3=(x1+2*x2)//3
    k=k+1
print(k, x2, x3)
    
