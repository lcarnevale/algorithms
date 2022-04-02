# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
This implementation does its best to follow the Robert Martin's Clean code guidelines.
The comments follows the Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

import time
import random
import numpy as np
import matplotlib.pyplot as plt
from merge_sort.merge_sort import merge_sort
from scipy.interpolate import make_interp_spline
from insertion_sort.insertion_sort import insertion_sort

__copyright__ = 'Copyright 2022, FCRlab at University of Messina'
__author__ = 'Lorenzo Carnevale <lcarnevale@unime.it>'
__credits__ = 'Algorithms and Data Structure, University of Messina'
__description__ = 'Sort Algorithms Comparison'

algorithms = {
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort
}

def create_array(dimension):
    data = list()
    for _ in range(dimension):
        data.append( random.randint(0, dimension) )
    return data

def execute(algorithm, data):
    start_time = time.time()
    algorithms[algorithm](data)
    end_time = time.time()
    return (end_time - start_time) * 1000

def main():
    times_insertion_sort = list()
    times_merge_sort = list()

    dimensions = range(2, 2000, 100)
    for dimension in dimensions:
        data = create_array(dimension)
        times_insertion_sort.append(execute("insertion_sort", data))
        times_merge_sort.append(execute("merge_sort", data))
    
    dimensions_smooth = np.linspace(min(dimensions),max(dimensions), 300)
    times_insertion_sort_smooth = make_interp_spline(dimensions, times_insertion_sort)(dimensions_smooth)
    times_merge_sort_smooth = make_interp_spline(dimensions, times_merge_sort)(dimensions_smooth)

    plt.plot(dimensions_smooth, times_insertion_sort_smooth, label='Insertion Sort')
    plt.plot(dimensions_smooth, times_merge_sort_smooth, label='Merge Sort')
    plt.title("Comparison of sort algorithms with random data")
    plt.xlabel("data dimension")
    plt.ylabel("time [ms]")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()