def insertionSort(array):
    #loop through the length of the array
    for step in range(1,len(array)):
        #set first element of the unsorted sub-set as the key
        key = array[step]
        #loop backward from the step index untill 
        #an element is found smaller than the key
        j = step -1
        while j>=0 and key < array[j]:
            #push all such elements to the right that are greater than the key
            array[j+1] = array[j]
            j -= 1
        #place the key right after the smaller element
        array[j+1] = key
    return array

arr = list(map(int, input('Enter an array: ').split()))

print('Insertion sort =>',insertionSort(arr))