# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2022, FCRlab at University of Messina'
__author__ = 'Lorenzo Carnevale <lcarnevale@unime.it>'
__credits__ = 'Algorithms and Data Structure, University of Messina'
__description__ = 'Quicksort'


def quicksort(data, leftmark, rightmark):
    """Quicksort implementation.

    QUICKSORT(A, p, r)
    if p<r
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q-1)
        QUICKSORT(A, q+1, r)

    Args:
        data (list): array to be sorted
        leftmark (int): starting index
        rightmark (int): ending index

    Returns
        (list) sorted array.
    """
    if leftmark < rightmark:
        pivot = partition(data, leftmark, rightmark)
        quicksort(data, leftmark, pivot - 1)
        quicksort(data, pivot + 1, rightmark)
    return data

def partition(data, leftmark, rightmark):
    """
    
    This function takes last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot

    PARTITION(A, p, r)
    x = A[r]
    i = p-1
    for j = p to r-1
        if A[j] <= x
            i = i + 1
            swap A[i] with A[j]
    swap A[i+1] with A[r]
    return i+1

    Args:
        data (list): array to be sorted
        leftmark (int):
        rightmark (int): 

    Returns:
        (int) position of the pivot
    """
    print("arr[] = %s" % (data))
    print("Indexes: %s" % '  '.join(str(i) for i in range(0,len(data))))
    pivot = data[rightmark] # pivot
    i = leftmark - 1 # index of smaller element
    print("\nleftmark = %s, rightmark = %s, pivot = arr[rightmark] = %s" % (leftmark, rightmark, pivot))
    print("Inizialize index of smaller element, i = %s" % (i))
    print("\nTraverse elements from j = leftmark to rightmark - 1")
    for j in range(leftmark, rightmark):
        if data[j] <= pivot: # if current element is smaller than or equal to pivot
            print("j = %s : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])" % (j))
            i += 1
            print("i = %s" % (i))
            data[i], data[j] = data[j], data[i]
            print("arr[] = %s, we swap %s and %s\n" % (data, data[j], data[i]))
        else:
            print("j = %s : Since arr[j] > pivot, do nothing\n" % (j))
    print("We come out of loop because j is now equal to rightmark-1")
    print("Finally we place pivot at correct position by swapping")
    print("arr[i+1] and arr[rightmark] (or pivot)")
    data[i + 1], data[rightmark] = data[rightmark], data[i + 1]
    print("arr[] = %s, we swap %s and %s" % (data, data[rightmark], data[i + 1]))
    print("\nNow %s is at its correct place. All elements smaller than" % (pivot))
    print("%s are before it and all elements greater than %s are after it\n" % (pivot, pivot))
    return i + 1

def main():
    unsorted_numbers = [2,8,7,1,3,5,6,4]
    leftmark, rightmark = 0, len(unsorted_numbers)-1
    print( quicksort(unsorted_numbers, leftmark, rightmark) )

if __name__ == '__main__':
    main()