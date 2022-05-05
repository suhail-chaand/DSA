def bubbleSort(array):
    #loop to iterate through the length of an array, 
    #i.e., number of iterations = length of the array 
    for i in range(len(array)):
        swapped = False
        #loop to compare and swap adjacent elements
        #skipping on the largest elements placed at the end
        #through each iteration
        for j in range(len(array)-1-i):
            #Use array[j] < array[j+1] for descending sort
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
        #Cancel further iterations if no swapping has occured in the iteration
        #indicating that the array is sorted
        if not swapped:
            break
    return array

arr = list(map(int,input('Enter an array: ').split()))

print(bubbleSort('Bubble sort =>',arr))