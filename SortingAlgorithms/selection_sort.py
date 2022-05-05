def selectionSort(array):
    #loop through the array length 
    for step in range(len(array)):
        #set first element of the unsorted sub-set as the minimum
        minimum = array[step]
        #loop through the unsorted sub-set to fetch its minimum
        for i in range(step+1,len(array)):
            if array[i] < minimum:
                minimum = array[i]
        #swap first element of the unsorted sub-set with the minimum
        (array[array.index(minimum)], array[step]) = (array[step], minimum)
    return array

arr = list(map(int, input('Enter an array: ').split()))

print('Selection sort =>',selectionSort(arr))