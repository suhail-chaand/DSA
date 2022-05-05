def mergeSort(array):
    if len(array) > 1:

        #array divided at r into two subarrays sa1 & sa2
        r = len(array)//2
        sa1 = array[:r]
        sa2 = array[r:]

        #recursively divide the array to obtain subarrays of all length=1
        mergeSort(sa1)
        mergeSort(sa2)

        #pointer i for sa1
        #pointer j for sa2
        #pointer k for merged array
        i = j = k = 0

        #until we reach either end of either sa1 or sa2, pick larger among
        #elements of sa1 and sa2 and place them in the correct position
        #in the merged array A[p..r]
        while i < len(sa1) and j < len(sa2):
            if sa1[i] < sa2[j]:
                array[k] = sa1[i]
                i += 1
            else:
                array[k] = sa2[j]
                j += 1
            k += 1

        #when we run out of elements in either sa1 or sa2,
        #pick up the remaining elements and put in merged array
        while i < len(sa1):
            array[k] = sa1[i]
            i += 1
            k += 1

        while j < len(sa2):
            array[k] = sa2[j]
            j += 1
            k += 1

arr = list(map(int,input('Enter an array: ').split()))

mergeSort(arr)
print('Merge sort =>',arr)