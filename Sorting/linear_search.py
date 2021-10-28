def linearSearch(array, key):
    for i in range(0,  len(array)):
        if (array[i] == key):
            return i
    return -1

arr = [18, 34, 21, 12, 98, 22, 14]
input_num = input("Enter a number: ")
result = linearSearch(arr, input_num)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
