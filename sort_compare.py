import time
import random

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end = time.time()
    return a_list, end - start


def shell_sort(a_list):
    start = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(a_list, startposition, sublistcount)
        sublistcount = sublistcount // 2
    end = time.time()
    return a_list, end - start


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return a_list, end - start


def get_me_random_list(n):
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def main():
    sizes = [500, 1000, 5000]
    
    for size in sizes:
        totals = {
            "Insertion Sort": 0.0,
            "Shell Sort": 0.0,
            "Python Sort": 0.0
        }

        for _ in range(100):
            # We need three fresh copies of the same random list 
            # so each algorithm sorts the exact same data.
            base_list = get_me_random_list(size)
            
            # 1. Insertion Sort
            list_copy = list(base_list)
            _, t = insertion_sort(list_copy)
            totals["Insertion Sort"] += t
            
            # 2. Shell Sort
            list_copy = list(base_list)
            _, t = shell_sort(list_copy)
            totals["Shell Sort"] += t
            
            # 3. Python Sort
            list_copy = list(base_list)
            _, t = python_sort(list_copy)
            totals["Python Sort"] += t

        print(f"--- Results for List Size {size} ---")
        for name, total_time in totals.items():
            avg_time = total_time / 100
            print(f"{name} took {avg_time:10.7f} seconds to run, on average")
        print()

if __name__ == "__main__":
    main()
