def insertion_sort(array=None):
    l = len(array)
    if l < 2:
        return
    for i in range(1,l,1):
        current = array[i]
        j = i-1
        while(j > -1 and current < array[j]):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current

if __name__ == "__main__":
    array = [9,8,7,6,5,4,3,2,1]
    insertion_sort(array)
    print("Sorted array is: ", array)