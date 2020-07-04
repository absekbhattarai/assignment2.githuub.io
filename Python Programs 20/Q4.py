n = int(input("enter number of item"))
list = []
x = id(list)
print(id(list))
for i in range(0, n):
    element = input("enter name: ")
    list.append(element)
list.sort()
print(list)
y = id(list)
print(y)


if x==y :
    print("The id for both are same")
else:
    print("The id for both are not same")



