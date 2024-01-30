import time
import timeit
import psutil
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(li):
    for i in range(1, len(li)):
        k = li[i]
        j = i - 1
        while j >= 0 and k < li[j]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = k

def selection_sort(li):
    l = len(li)
    for i in range(l - 1):
        # Find the minimum element in the unsorted array
        m = i
        for j in range(i + 1, l):
            if li[j] < li[m]:
                m = j

        # Swap the minimum element with the 1st element
        li[i], li[m] = li[m], li[i]

def bubble_sort(li):
    l = len(li)

    for i in range(l):
        for j in range(0, l - i - 1):
            # Swap if the element is greater than the next element
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

def BA(algorithm, arr):
    sc = f"""
import numpy as np
import psutil
import time
from __main__ import {algorithm}

arr = {arr}
"""

    gd = {'arr': None, 'insertion_sort': insertion_sort, 'selection_sort': selection_sort, 'bubble_sort': bubble_sort}

    exec(sc, gd)

    # Call the sorting algorithm using the passed parameter
    sort_algo = gd[algorithm]
    sort_algo(arr)

    no_of_iters = 100000
    algorithm_time = timeit.timeit(stmt=lambda: sort_algo(arr), number=no_of_iters)

    time.sleep(0.1)

    cpu_info = psutil.cpu_percent()
    ram_info = psutil.virtual_memory()

    return {
        "time_taken": algorithm_time / no_of_iters,
        "sorted_array": arr.copy(),  # Add the sorted array to the output
        "cpu_info": cpu_info,
        "ram_info": ram_info,
    }

if __name__ == "__main__":
    arrays = [
        [5, 3, 8, 2, 7],
        [12, 6, 1, 15, 9, 13, 17, 2, 8, 10],
        [20, 10, 8, 15, 5, 1, 2, 3, 4, 7, 5, 12, 13, 9, 17, 16, 11, 19, 21, 24]
    ]

    algorithms = ["insertion_sort", "selection_sort", "bubble_sort"]

    algo_data = {algorithm: [] for algorithm in algorithms}

    for array in arrays:
        for algorithm in algorithms:
            algo_data[algorithm].append(BA(algorithm, array.copy()))

    # Display the results
    for algorithm in algorithms:
        print(f"--> {algorithm} <--")
        for data in algo_data[algorithm]:
            print(f"Sorted Array: {data['sorted_array']}, Time Taken: {data['time_taken']} seconds, CPU Usage: {data['cpu_info']}%, RAM Usage: {data['ram_info'].percent}%")
        #print()
        print("RAM:- 8GB")
        print()

    # Plotting
    for algorithm in algorithms:
        plt.plot([len(data['sorted_array']) for data in algo_data[algorithm]], [data['time_taken'] for data in algo_data[algorithm]], marker='*', label=algorithm)

    plt.xlabel("Array size")
    plt.ylabel("Time (seconds)")
    plt.title("Algorithm Runtime Comparison for Arrays of Different Size")
    plt.legend()
    plt.show()

'''Code by
SANDEEP SANAGALA
1002157289'''
