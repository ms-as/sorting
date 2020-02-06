import matplotlib.pyplot as plt 
import matplotlib.animation as anim
import time
import numpy as np

#requires: python 3.3 or higher, due to yield feature

#define of sort algorithms 
def bubbleSort(arr):
    """Bbubble sort implementation"""

    if len(arr) == 1:
        return arr

    not_swapped = False

    for i in range(len(arr)-1):
        if not_swapped:
            break
        
        not_swapped = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                fun_swap(arr, j, j+1)
                not_swapped = False
            yield arr

def mergeSort(arr, start, end):
    """ Merge sort implementation"""
    if start >= end:
        return arr

    mid = start +((end - start + 1)//2)-1
    yield from mergeSort(arr, start, mid)
    yield from mergeSort(arr, mid+1, end)
    yield from final_merge(arr, start, mid, end)
    yield arr

def quickSort(arr, start, end):
    """ Quick sort implementation"""

    if end <= start:
        return arr
    
    pivot = arr[end]
    indeks = start

    for i in range(start, end):
        if arr[i] < pivot:
            fun_swap(arr,i,indeks)
            indeks += 1
        yield arr
    fun_swap(arr, end, indeks)
    yield arr

    yield from quickSort(arr, start, indeks - 1)
    yield from quickSort(arr, indeks + 1, end)


def insertionSort(arr):
    """ Intertion sort implementation"""

    for i in range (1, len(arr)):
        k = i
        while k > 0 and arr[k - 1] > arr[k]:
            fun_swap(arr, k, k - 1)
            k -= 1
            yield arr

def selectionSort(arr):
    """ Selection sort implementation"""
    if len(arr) == 1:
        return arr
    
    for i in range(len(arr)):
        minimum = arr[i]
        minimum_index = i
        for j in range (i, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                minimum_index = j
            yield arr
        fun_swap(arr, i, minimum_index)
        yield arr


def coctailSort(arr, start, end):
    if len(arr) == 1:
        return arr
    
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end): 
            if (arr[i] > arr[i + 1]) : 
                fun_swap(arr, i, i+1)
                swapped = True
            yield arr
            
        if not swapped:
            yield arr

        swapped = False

        end -= 1

        for i in range(end-1, start-1, -1): 
            if (arr[i] > arr[i + 1]): 
                fun_swap(arr, i, i+1)
                swapped = True
                yield arr
        
        start = start + 1

#Helping fucntions here 

def final_merge(arr,start, mid, end):
    """Function for merge sort"""

    merged = []
    L_index = start
    R_index = mid +1

    while L_index <= mid and R_index <= end:
        if arr[L_index]< arr[R_index]:
            merged.append(arr[L_index])
            L_index += 1
        else:
            merged.append(arr[R_index])
            R_index += 1


    while L_index <= mid:
        merged.append(arr[L_index])
        L_index += 1
    while R_index <= end:
        merged.append(arr[R_index])
        R_index += 1

    for i, val in enumerate(merged):
        arr[start + i] = val
        yield arr


def fun_swap(arr, i, j):
    """Function  to swapping neighbour elements (i, i+1) in array """
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]

#plot functions here!

def next_frame(arr, poles, iterations):
    for poles, value in zip(poles, arr):
        poles.set_height(value)
    iterations[0] += 1
    text.set_text("Number of operations: {}".format(iterations[0])) 


if __name__ == "__main__":

    number_of_int = int(input("Enter number: "))
    sort_method = input("Enter sorting method:\n(b)ubble\n(m)erge \
        \n(q)uick\n(i)nsertion\n(s)election\n(c)octail\n")
    
    arr = [x+1 for x in range(number_of_int)]
    np.random.randint(time.time())
    np.random.shuffle(arr)

    if sort_method == "b":
        title = "Bubble_Sort"
        fra = bubbleSort(arr)
    elif sort_method == "m":
        title = "Merge sort"
        fra = mergeSort(arr, 0, number_of_int - 1)
    elif sort_method == "q":
        title = "QuickSort"
        fra = quickSort(arr, 0, number_of_int - 1)
    elif sort_method == "i":
        title = "Insertion_Sort"
        fra = insertionSort(arr)
    elif sort_method == "s":
        title = "Selection_Sort"
        fra = selectionSort(arr)
    else:
        title = "Coctail_Sort"
        fra = coctailSort(arr, 0, number_of_int - 1)

    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_ = ax.bar(range(len(arr)), arr, align="edge")

    ax.set_xlim(0, number_of_int)
    ax.set_ylim(0, int(1.1 * number_of_int))

    text = ax.text( 0.03, 1, "", transform=ax.transAxes)

    iterations = [0]
    animations = anim.FuncAnimation(
        fig, func=next_frame, fargs=(bar_, iterations), 
        frames=fra, interval = 1, repeat = False
        )
    animations.save("{}.gif".format(title), writer = 'imagemagick')
    plt.show()