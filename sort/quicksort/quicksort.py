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

import sys
import logging


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
    logging.info("arr[] = %s" % (data))
    logging.info("Indexes: %s" % '  '.join(str(i) for i in range(0,len(data))))
    pivot = data[rightmark] # pivot
    i = leftmark - 1 # index of smaller element
    logging.info("\nleftmark = %s, rightmark = %s, pivot = arr[rightmark] = %s" % (leftmark, rightmark, pivot))
    logging.info("Inizialize index of smaller element, i = %s" % (i))
    logging.info("\nTraverse elements from j = leftmark to rightmark - 1")
    for j in range(leftmark, rightmark):
        if data[j] <= pivot: # if current element is smaller than or equal to pivot
            logging.info("j = %s : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])" % (j))
            i += 1
            logging.info("i = %s" % (i))
            data[i], data[j] = data[j], data[i]
            logging.info("arr[] = %s, we swap %s and %s\n" % (data, data[j], data[i]))
        else:
            logging.info("j = %s : Since arr[j] > pivot, do nothing\n" % (j))
    logging.info("We come out of loop because j is now equal to rightmark-1")
    logging.info("Finally we place pivot at correct position by swapping")
    logging.info("arr[i+1] and arr[rightmark] (or pivot)")
    data[i + 1], data[rightmark] = data[rightmark], data[i + 1]
    logging.info("arr[] = %s, we swap %s and %s" % (data, data[rightmark], data[i + 1]))
    logging.info("\nNow %s is at its correct place. All elements smaller than" % (pivot))
    logging.info("%s are before it and all elements greater than %s are after it\n" % (pivot, pivot))
    return i + 1

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    unsorted_numbers = [2,8,7,1,3,5,6,4]
    leftmark, rightmark = 0, len(unsorted_numbers)-1
    logging.info( quicksort(unsorted_numbers, leftmark, rightmark) )

if __name__ == '__main__':
    main()