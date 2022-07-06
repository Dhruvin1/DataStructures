def quicksort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


array = [12, 3, 4, 5, 6, 8, 9, 6, 53, 6, 90, 7, 8, 6, 5, 4, 7]
print("The initial array is: ", array)
sorted_array = quicksort(array)
print("The sorted array is: ", sorted_array)
