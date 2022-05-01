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
__description__ = 'Heapsort'


import sys
import logging

def get_parent_position(i):
        return i/2

def get_left_child_position(i):
        return 2*i

def get_right_child_position(i):
        return (2*i)+1

def max_heapify(data, i, heapsize):
    largest = i
    left = get_left_child_position(i)
    right = get_right_child_position(i)
    logging.info("largest = i = %s, left = 2*i =  %s, right = (2*i)+1 = %s" % (largest, left, right))

    logging.info("left (%s) < heapsize (%s) and data[%s] > data[%s]" \
        % (left, heapsize, left, i))
    if left < heapsize and data[left] > data[i]: 
        largest = left
        logging.info("left child of root exists and is greater than root, largest = left = %s" % (largest))

    logging.info("right (%s) < heapsize (%s) and data[%s] > data[%s]" \
         % (right, heapsize, right, largest))
    if right < heapsize and data[right] > data[largest]:
        largest  = right
        logging.info("right child of root exists and is greater than root, largest = right = %s" % (largest))

    logging.info("i (%s) != largest (%s) -> %s"\
         % (i, largest, i != largest))
    if i != largest:
        data[i], data[largest] = data[largest], data[i]
        logging.info("arr[] = %s, we swap %s and %s" % (data, data[i], data[largest]))
        logging.info("heapify the root\n")
        max_heapify(data, largest, heapsize)

def build_max_heap(data, heapsize):
    logging.info("Since last parent will be at ((n//2)-1) = %s, we can start at that location" % (heapsize//2 - 1))
    for i in range(heapsize//2 - 1, -1, -1):
        logging.info("\ni = int(heapsize/2) = %s : execute max_heapify" % (i))
        max_heapify(data, i, heapsize)
    
def heapsort(data):
    heapsize = len(data)
    logging.info("arr[] = %s, heapsize = %s" % (data, heapsize))
    logging.info("Indexes:  %s\n" % '  '.join(str(i) for i in range(0,len(data))))

    logging.info("Let's now build a max heap")
    build_max_heap(data, heapsize)
    logging.info("\narr[] = %s" % (data))
    logging.info("Indexes: %s\n" % '  '.join(str(i) for i in range(0,len(data))))

    for i in range(len(data)-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        logging.info("i=%s : arr[] = %s, we swap %s and %s\n" % (i, data, data[0],data[i]))
        max_heapify(data, 0, i)
    
    return data

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    unsorted_data = [4,1,3,2,16,9,10,14,8,7]
    heapsort(unsorted_data)

if __name__ == '__main__':
    main()




