def countInversion(arr):
    global c
    c = 0
    mergeSort(arr)
    return c

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        merge_two_sorted_arrays(left, right, arr)

def merge_two_sorted_arrays(arr1, arr2, arr):
    global c
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    i = j = k = 0

    while i < len_arr1 and j < len_arr2:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else: # arr1[i] > arr2[j]
            c += len_arr1 - i #NOTE We consider arr1[i] and all elements after it. Because if arr1[i] > arr2[j], then arr1[i+1], arr1[i+2], ... arr1[i+n] > arr2[j]. We consider all elements after
            arr[k] = arr2[j]
            j += 1
        k += 1
        
    while i < len_arr1:
        arr[k] = arr1[i]
        i += 1
        k += 1
        
    while j < len_arr2:
        arr[k] = arr2[j]
        j += 1
        k += 1
    # print(arr)

arr = [5, 3, 1, 2]

print(countInversion(arr))
