list1=[1,2,3,78,98]
list2=[3,6,87,9,12,5]
print("list1 :",list1)
print("list2 :",list2)
print("length of list1 :",len(list1))
print("length of list2 :",len(list2))
if len(list1)==len(list2):
    print("length of two list are same")
else:
    print("not same length")
print("sum of the list1:",sum(list1))
print("sum of the list2:",sum(list2))
if sum(list1)==sum(list2):
    print("sum of 2 list are same")
else:
    print("not same sum")
check = any(item in list1 for item in list2)
print("any value occur in both : ", check)