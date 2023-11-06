n=int(input("enter the number :"))
f1, f2 = 0, 1
print("fibonaci SERIES:")
print(f1)
print(f2)
for i in range (1,n-1):
    fib=f1+f2
    print(fib)
    f1,f2=f2,fib