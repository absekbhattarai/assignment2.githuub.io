import csv
import os

def csv_file():
    path = 'D:\INSIGHTS WORKSHOP\Python Programs 20'

    fields = ('Name','Address','Age')
    filename = input("Enter file name: ")+'.csv'
    csvFilename = os.path.join(path,filename)
    my_tuple = ()
    list = []
    count = int(input("Enter number of items to be written in File: "))
    for i in range(0,count):
        data  = input("Enter Name , Address , Age seperated by: ")
        my_tuple = tuple(data.split())
        list.append(my_tuple)
    print(list)
    with open(csvFilename,'w',newline='') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(fields)
        writer.writerows(list)

csv_file()