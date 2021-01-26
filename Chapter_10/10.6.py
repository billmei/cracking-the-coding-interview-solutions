# Sort Big File
# How would you sort a 20 GB file with one string per line?

# Assumptions
# Example
# Algo
# Code
# Test

# Idea 1: Distributed Sort.
# Basically merge sort, except each worker node gets its own copy of an array to do 
# a sub sort using insertion sort.
# Then, the coordinator performs the merge operation (with a barrier)

import concurrent.futures
import numpy as np

data = [24, 28, 1, 9, 10, 29, 16, 18, 13, 11, 6, 19, 27, 8, 17, 22, 14, 25, 21, 2, 4]

NUM_THREADS = 4

def split_chunks(data):
    return np.array_split(data, NUM_THREADS)

def worker(subarray):
    # Insertion sort
    return sorted(subarray)

def distributed_merge_sort(data):
    chunks = split_chunks(data)

    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        executor.map(split_chunks, chunks)
    # At the end, merge the chunks


# Solution: We don't want to bring the whole file into memory
#           Instead of threads, bring only one chunk of the file into memory
#           at a time (external sort.)

