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
__description__ = 'Mergesort'


import sys
import logging


def merge(s1, s2, s):
    logging.info("S_left[]: %s, S_right[]: %s, S[]: %s" % (s1, s2, s))
    logging.info("S_left[].length: %s, S_right[].length: %s, S[].length: %s" % (len(s1), len(s2), len(s)))
    
    i = j = 0
    logging.info("while: i = j = 0, i+j < S[].length ? %s" % (i + j < len(s))) 
    while i + j < len(s):
        logging.info("  i = %s, j = %s, j == S_right[].length OR (i < S_left[].length AND S_left[i] < S_right[j])" % (i,j))
        try:
            logging.info("  i = %s, j = %s, %s OR (%s AND %s)" % (i,j, j == len(s2), i < len(s1), s1[i] < s2[j]))
        except:
            logging.info("  i = %s, j = %s, out of range" % (i, j))

        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
            logging.info("    i = %s, j = %s, swap S[i+j] = S[%s] with S_left[i] = S_left[%s], i++" % (i, j, i+j, i))
        else:
            s[i+j] = s2[j]
            j += 1
            logging.info("    i = %s, j = %s, swap S[i+j] = S[%s] with S_right[j] = S_right[%s], j++" % (i, j, i+j, j))
        logging.info("    S_left[]: %s, S_right[]: %s, S[]: %s" % (s1, s2, s))
        logging.info("while: i = %s, j = %s, i+j < S[].length ? %s" % (i, j, i + j < len(s))) 
    logging.info("\n") 
    return s

def merge_sort(data):
    logging.info("S[]:     %s" % (data))
    logging.info("Indexes:   %s" % '   '.join(str(i) for i in range(0,len(data))))
    
    n = len(data)
    if n < 2:
        logging.info("Stop recursion\n")
        return
    #logging.info("\n")
    
    mid = n // 2
    logging.info("left = 0, mid = %s, right = %s\n" % (mid, n-1))
    
    data_left = data[0:mid]
    logging.info("Call mergesort on S[0:mid-1] = S[0:%s]" % (mid-1))
    merge_sort(data_left)

    data_right = data[mid:n]
    logging.info("Call mergesort on S[mid:N] = S[%s:%s]" % (mid, n))
    merge_sort(data_right)

    merge(data_left, data_right, data)

    return data

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    unsorted_numbers = [16,10,21,45]
    print( merge_sort(unsorted_numbers) )


if __name__ == '__main__':
    main()
