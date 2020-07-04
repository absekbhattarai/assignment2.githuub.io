tuple1 = ('Abhishek', 'Bhattarai', '22')
print(tuple1)
list1 = []
list1.append(tuple1)

print(list1)
final_list = []
line = input("Enter the list of tuples:\n")
while (line != ''):
    final_list.append(tuple(line.split()))
    line = input("Press enter to proceed")
print(final_list)
list3 = list1 + final_list
print("final list")
print(list3)
list3.sort(key = lambda x: x[0])
print("list sorted by first name")
print(list3)
list3.sort(key = lambda x: x[1])
print("list sorted by last name")
print(list3)
list3.sort(key = lambda x: x[2])

print("list sorted by age")
print(list3)