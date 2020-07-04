import csv

def read_file():

    file = input("Enter file that you want to retrieve: ")
    filename = file + '.csv'

    with open (filename,'r') as data:
        reader  = csv.DictReader(data)
        listItem = list(reader)

    print(listItem)


read_file()