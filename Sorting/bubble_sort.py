# Bubble sort in python

# Function bubbe sort
def bubble_sort(array):
    for i in range(len(array)-2):
        
        for j in range(0,len(array)-1-i):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp



array = [int(item) for item in input("Enter the list items : ").split()]

bubble_sort(array)
print("Sorted list :")
print(array)
