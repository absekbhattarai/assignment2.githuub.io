index = 0
filename = input("Enter a filename with extension: ")
index = filename.find('.')
s1= slice(index)
print("File name : ",filename[s1])



