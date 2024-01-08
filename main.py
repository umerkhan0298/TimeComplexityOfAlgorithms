import math
import timeit
import random

def linear_search(arr, x):
    
    start_time = timeit.default_timer()
    for i in range(len(arr)):
        if arr[i] == x:
            end_time = timeit.default_timer()
            return i, (end_time - start_time)*1000000
    end_time = timeit.default_timer()
    return -1, (end_time - start_time)*1000000

def binary_search(arr, x):
    
    start_time = timeit.default_timer()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            end_time = timeit.default_timer()
            return mid, (end_time - start_time)*1000000
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    end_time = timeit.default_timer()
    return -1, (end_time - start_time)*1000000

def ternary_search(arr, x):
    
    start_time = timeit.default_timer()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if arr[mid1] == x:
            end_time = timeit.default_timer()
            return mid1, (end_time - start_time)*1000000
        elif arr[mid2] == x:
            end_time = timeit.default_timer()
            return mid2, (end_time - start_time)*1000000
        elif arr[mid1] > x:
            high = mid1 - 1
        elif arr[mid2] < x:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    end_time = timeit.default_timer()
    return -1, (end_time - start_time)*1000000

def jump_search(arr, target):
    
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    start_time = timeit.default_timer()
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            end_time = timeit.default_timer()
            return -1, (end_time - start_time)*1000000

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            end_time = timeit.default_timer()
            return i, (end_time - start_time)*1000000
    
    end_time = timeit.default_timer()
    return -1, (end_time - start_time)*1000000

if __name__ == "__main__":

    list_length = 1000000
    input_list = [random.randint(1, list_length) for _ in range(list_length)]
    # print(input_list)
    search_number = 10
    input_list = sorted(input_list)

    linear_search_index, linear_search_time = linear_search(input_list, search_number)
    print(f"Linear Search Result: Index {linear_search_index}, Time {linear_search_time} microseconds")

    binary_search_index, binary_search_time = binary_search(input_list, search_number)
    print(f"Binary Search Result: Index {binary_search_index}, Time {binary_search_time} microseconds")

    ternary_search_index, ternary_search_time = ternary_search(input_list, search_number)
    print(f"Ternary Search Result: Index {ternary_search_index}, Time {ternary_search_time} microseconds")

    # jump_search_index, jump_search_time = jump_search(input_list, search_number)
    # print(f"Jump Search Result: Index {jump_search_index}, Time {jump_search_time} microseconds")