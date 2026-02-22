import time
import random

def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
            
    end = time.time()
    return found, end - start


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
                
    end = time.time()
    return found, end - start


def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
                
    end = time.time()
    return found, end - start


def binary_search_recursive(a_list, item, start_time=None):
    # Initialize timer on the first call
    if start_time is None:
        start_time = time.time()
        
    if len(a_list) == 0:
        return False, time.time() - start_time
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True, time.time() - start_time
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item, start_time)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item, start_time)


def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def main():
    sizes = [500, 1000, 5000]
    search_item = 99999999
    
    for size in sizes:
        # Dictionary to keep track of total time for each algorithm
        totals = {
            "Sequential Search": 0.0,
            "Ordered Sequential Search": 0.0,
            "Binary Search Iterative": 0.0,
            "Binary Search Recursive": 0.0
        }

        for _ in range(100):
            # 1. Generate list for this iteration
            mylist = get_me_random_list(size)
            
            # 2. Benchmark Sequential Search (Unordered)
            _, time_taken = sequential_search(mylist, search_item)
            totals["Sequential Search"] += time_taken
            
            # 3. Sort the list for the other three algorithms
            mylist.sort()
            
            # 4. Benchmark the rest
            _, time_taken = ordered_sequential_search(mylist, search_item)
            totals["Ordered Sequential Search"] += time_taken
            
            _, time_taken = binary_search_iterative(mylist, search_item)
            totals["Binary Search Iterative"] += time_taken
            
            _, time_taken = binary_search_recursive(mylist, search_item)
            totals["Binary Search Recursive"] += time_taken

        # Print results for this size category
        print(f"--- Results for List Size {size} ---")
        for name, total_time in totals.items():
            avg_time = total_time / 100
            print(f"{name} took {avg_time:10.7f} seconds to run, on average")
        print()

if __name__ == "__main__":
    main()
