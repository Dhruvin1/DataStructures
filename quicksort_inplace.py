def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]
    i = i+1
    array[i], pivot = pivot, array[i]
    return i

def quicksort(array, low, high):
    if(low<high):
        pivot = partition(array,low,high)
        quicksort(array,low,pivot-1)
        quicksort(array,pivot+1,high)

if __name__ == "__main__":
    array = [1,2,45,7,34,6,8,9,5,3,5,76,8,9,6,5,4,3,3,4,5,6,7,8,9,8,7,6,65,5,4,4,3,3,4,5,6,7,7,8,8,7,655,7,7,8,6,5,4,456,6,100,76,6,7,7,6]
    print("Unsorted array: ",array)
    l = len(array)
    quicksort(array,0,l-1)
    print("Sorted array: ",array)