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
from merge_sort import merge_sort
from scipy.interpolate import make_interp_spline

__copyright__ = 'Copyright 2022, FCRlab at University of Messina'
__author__ = 'Lorenzo Carnevale <lcarnevale@unime.it>'
__credits__ = 'Algorithms and Data Structure, University of Messina'
__description__ = 'Merge Sort Comparison'

def create_array(dimension):
    data = list()
    for _ in range(dimension):
        data.append( random.randint(0, dimension) )
    return data

def main():
    times_random = list()
    times_better_case = list()
    times_worste_case = list()

    dimensions = range(2, 10000, 1000)
    for dimension in dimensions:
        data = create_array(dimension)

        start_time = time.time()
        data_sorted = merge_sort(data)
        end_time = time.time()
        times_random.append( (end_time - start_time) * 1000 )

        start_time = time.time()
        merge_sort(data_sorted)
        end_time = time.time()
        times_better_case.append( (end_time - start_time) * 1000 )

        data_sorted_reverse = data_sorted[::-1]
        start_time = time.time()
        merge_sort(data_sorted_reverse)
        end_time = time.time()
        times_worste_case.append( (end_time - start_time) * 1000 )
    
    dimensions_smooth = np.linspace(min(dimensions),max(dimensions), 300)
    times_better_case_smooth = make_interp_spline(dimensions, times_better_case)(dimensions_smooth)
    times_random_smooth = make_interp_spline(dimensions, times_random)(dimensions_smooth)
    times_worste_case_smooth = make_interp_spline(dimensions, times_worste_case)(dimensions_smooth)

    plt.plot(dimensions_smooth, times_better_case_smooth, label='Sorted Data')
    plt.plot(dimensions_smooth, times_random_smooth, label='Unsorted Data')
    plt.plot(dimensions_smooth, times_worste_case_smooth, label='Reverse Sorted Data')
    plt.title("Comparison of Merge Sort")
    plt.xlabel("data dimension")
    plt.ylabel("time [ms]")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()