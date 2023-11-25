def bubblesort(array = None):
    length = len(array)
    if length < 2:
        return
    for i in range(0,length,1):
        for j in range(0,length-i-1,1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


if __name__ == "__main__":
    array = [9,8,7,6,5,4,3,2,1]
    bubblesort(array)
    print("Sorted array is: ", array)
