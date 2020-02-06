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
    text.set_text("# of operations: {}".format(iterations[0])) 


if __name__ == "__main__":

    number_of_int = int(input("Enter number: "))
    
    arr = [x+1 for x in range(number_of_int)]
    np.random.randint(time.time())

    np.random.shuffle(arr)

    fig, ax = plt.subplots()
    ax.set_title("BubbleSort")

    bar_ = ax.bar(range(len(arr)), arr, align="edge")

    ax.set_xlim(0, number_of_int)
    ax.set_ylim(0, int(1.1 * number_of_int))

    text = ax.text( 0.03, 1, "", transform=ax.transAxes)

    iterations = [0]
    """animations = anim.FuncAnimation(
        fig, func=next_frame, fargs=(bar_, iterations), 
        frames=bubbleSort(arr), interval = 10, repeat = False
        )""" #można odkomentować i sprobowac jak wyglada dla bubble
    animations = anim.FuncAnimation(
        fig, func=next_frame, fargs=(bar_, iterations), 
        frames=quickSort(arr, 0, number_of_int-1), interval = 10, repeat = False
        )
    plt.show()



