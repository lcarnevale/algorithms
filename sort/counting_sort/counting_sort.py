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
__description__ = 'Counting Sort'


import sys
import logging

def counting_sort(A):
    logging.info("A[]  =  %s" % (A))
    logging.info("Indexes: %s\n" % '  '.join(str(i) for i in range(0,len(A))))

    k = max(A)
    logging.info("k = max(A) = %s" % (k))
    logging.info("Initialize C[] of dimension k+1 = %s with all zeros" % (k+1))
    C = [0 for _ in range(0, k+1)]
    logging.info("Initialize B[] of dimension len(A) = %s with all zeros\n" % (len(A)))
    B = [0 for _ in range(0, len(A))]

    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
        logging.info("j = %s : increment C in position A[j] of 1 unit, C[A[j]] = C[%s] = %s" % (j, A[j], C[A[j]]))
    logging.info("\nC[] = %s\n" % (C))

    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
        logging.info("i = %s : increment C[%s] of C[%s] units, C[%s] = %s" % (i, i-1, i, i, C[i]))
    logging.info("\nC[] = %s\n" % (C))

    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        logging.info("j = %s : assign B[C[A[j]]-1] = B[C[%s]-1] = B[%s] = A[j] = %s" % (j, A[j], C[A[j]]-1, A[j]))
        C[A[j]] -= 1
        logging.info("j = %s : assign C[A[j]] = C[A[j]] - 1 = C[%s] - 1 = %s" % (j, A[j], C[A[j]]))
    
    return B    


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    unsorted_numbers = [2,5,3,0,2,3,0,3]
    logging.info( counting_sort(unsorted_numbers) )

if __name__ == '__main__':
    main()