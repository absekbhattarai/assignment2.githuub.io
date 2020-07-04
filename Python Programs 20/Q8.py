def is_prime(x):

    num= int(input("Enter a number: "))
    if (num > 1):
        divisor = 2
        for i in range(divisor,num):
            if (num % i) == 0:
                return False
    else:
        return False
    return True
print ("Is PRIME: ",is_prime('num'))
