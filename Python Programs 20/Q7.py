tuple1 = ('Absek', 'Bhattarai', '22')
tuple2 = ('Aayush', 'Bhattarai', '18')
tuple3 = ('Ram', 'Shah', '24')
tuple4 = ('Shyam', 'Shrestha', '17')

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

list1 = []
list2 = []
list3 = []
list4 = []
list1.append(tuple1)
list2.append(tuple2)
list3.append(tuple3)
list4.append(tuple4)
list5 = []
list5 = list1 + list2 + list3 + list4
print(list5)

res = sum(int(i[2]) for i in list5)
average_age = res/4
print("average age is ", average_age)
for i in list5:
    if int(i[2]) >= 18 :
        print("%s is older than 20" %i[0])
    elif int(i[2]) < 18:
        print("%s is younger than 20" %i[0])
    else:
        print("no age assigned")
