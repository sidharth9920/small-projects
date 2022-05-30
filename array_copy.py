def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
 
# Function to left rotate arr[] of size n by d
 
 
def leftRotate(arr, d):
 
    if d == 0:
        return
    n = len(arr)
    # in case the rotating factor is
    # greater than array length
    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
 
# Function to print an array
 
def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i],end=' ')
 
 
# Driver function to test above functions
n=int(input("enter the lenth of array :"))
arr = list(range(0,n))
n = len(arr)
d = int(input("Enter the number of rotations :"))
 
leftRotate(arr, d)  # Rotate array by 2
printArray(arr)