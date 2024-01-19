import random

#Generate 3 arrays, one already sorted, one random, and one in reverese
def generate_arrays():
    n = random.randint(100, 200)
    array1 = random.sample(range(1, 100000), n)
    array2 = random.sample(range(1, 100000), n)
    array3 = random.sample(range(1, 100000), n)

    array1.sort()
    array3.sort(reverse=True)

    return array1, array2, array3

#Generate 3 sorting algorithms that have different complexity for : BC, AC, WC
#The algorithms are : Bubble Sort, Merge Sort, Quick Sort

#Bubble Sort
def bubble_sort(arr):
    steps = 0
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            steps += 1
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return steps

#Merge Sort
def merge_sort(arr):
    steps = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        steps += merge_sort(left_half)
        steps += merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            steps += 1
            if left_half[i] < right_half[j]:
                steps += 1
                arr[k] = left_half[i]
                i += 1
            else:
                steps += 1
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            steps += 1
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            steps += 1
            arr[k] = right_half[j]
            j += 1
            k += 1

    return steps


#do a heap sort
def heapify(arr, n, i):
    steps = 0
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    steps += 1
    if l < n and arr[i] < arr[l]:
        largest = l

    steps += 1
    if r < n and arr[largest] < arr[r]:
        largest = r

    steps += 1
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps += heapify(arr, n, largest)

    return steps

def heap_sort(arr):
    steps = 0
    n = len(arr)

    for i in range(n, -1, -1):
        steps += heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps += heapify(arr, i, 0)

    return steps

def recursive_selection_sort(arr, steps=0):
    if len(arr) <= 1:
        return arr, steps
    
    # Find the minimum element in the unsorted part
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
        steps += 1
    
    # Swap the found minimum element with the first element
    arr[0], arr[min_index] = arr[min_index], arr[0]
    steps += 1
    
    # Sort the rest of the array (excluding the first element")
    sorted_arr, steps = recursive_selection_sort(arr[1:], steps)
    
    return [arr[0]] + sorted_arr, steps


#Preety-print
def printings(array1, array2, array3):
    min_best_case = min(array1[0], min(array2[0], array3[0]))
    min_average_case = min(array1[1], min(array2[1], array3[1]))
    min_worst_case = min(array1[2], min(array2[2], array3[2]))
    print('\n')
    print(f"The min. no. of steps for Best Case :{min_best_case} ")
    print(f"The min. no. of steps for Average Case :{min_average_case} ")
    print(f"The min. no. of steps for the Worst Case :{min_worst_case} ")

    print('\n')

    print("------- Bubble Sort -------")
    print(f"BC:{array1[0]} , AC:{array1[1]}, WC:{array1[2]}")
    print('\n')

    print("------- Merge Sort -------")
    print(f"BC:{array2[0]} , AC:{array2[1]}, WC:{array2[2]}")
    print('\n')

    print("------- Recursive Selection Sort -------")
    print(f"BC:{array3[0]} , AC:{array3[1]}, WC:{array3[2]}")
    print('\n')
