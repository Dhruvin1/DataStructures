def quicksort(array, low, high):
    print("Input quicksort array args: {} {} {}".format(array, low, high))
    if (low<high):
        pi = partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array, pi+1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low -1
    for j in range(low,high):
        if(array[j]<=pivot):
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

array = [10,9,8,7,6,5,4,3,2,1]
quicksort(array,0,9)
print(array)