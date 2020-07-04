
list = []
n = int(input("enter the number of friends name you want to enter :"))
for i in range(0, n):
    element = input("enter name: ")
    list.append(element)
print(list)
print("This program search for the name 'John'")
if 'john' in list :
    print("John is in list")
else:
    print("John is not found")