def quicksort(array):
    low = []
    mid = []
    high = []
    length = len(array)
    if length > 1:
        pivot = array[length-1]
        for element in array:
            if element < pivot:
                low.append(element)
            elif element > pivot:
                high.append(element)
            else:
                mid.append(element)
        return quicksort(low)+mid+quicksort(high)
    else:
        return array

if __name__ == "__main__":
    array = [1,2,45,7,34,6,8,9,5,3,5,76,8,9,6,5,4,3,3,4,5,6,7,8,9,8,7,6,65,5,4,4,3,3,4,5,6,7,7,8,8,7,655,7,7,8,6,5,4,456,6,100,76,6,7,7,6]
    print("Unsorted array: ",array)
    l = len(array)
    new_array = quicksort(array)
    print("Sorted array: ",new_array)
