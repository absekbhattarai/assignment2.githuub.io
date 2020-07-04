def palindrome(str):
    str = input("Enter a string: ")
    reverse_string = str[::-1]
    if (str == reverse_string):
        return True
    else:
        return False
print("IS PALINDROME:",palindrome('str'))