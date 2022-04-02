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
__description__ = 'Insertion Sort'

def insertion_sort(a):
    for j in range(1,len(a)): 
        key = a[j]
        i = j
        while i > 0 and a[i-1] > key:
            a[i] = a[i-1]
            i = i - 1 
        a[i] = key 
    return a

def main():
    unsorted_numbers = [4,8,3,6,0,1,3]
    print( insertion_sort(unsorted_numbers) )

    unsorted_characters = ['g','t','j','a','u']
    print( insertion_sort(unsorted_characters) )

if __name__ == '__main__':
    main()