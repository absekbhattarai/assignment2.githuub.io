
def binary_search(arr,x):
    arr = input("Enter the number to be entered in list seperated by commas: ")
    x = int(input("Enter the number to be searched: "))
    arr = arr.split(',')
    arr = [int(i) for i in arr]
    arr.sort()
    print(arr)
    low= 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1

result = binary_search('arr', 'x')

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")