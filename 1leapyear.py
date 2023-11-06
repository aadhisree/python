a=int(input("Enter the starting year:"))
b=int(input("Enter the final year:"))
print("Leap year are:")
for i in range(a,b):
    if(i%4==0) and (i%100 !=0) or  (i%400== 0):
        print(i)