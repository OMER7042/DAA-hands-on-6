# The quicksort logic in this code selects a random element as pivot element and then sorts the array using it.

import random as randpiv

def random_pivot_quicksort(array):
    if len(array) <= 1:
        return array
    pivot = randpiv.choice(array)
    lesser = [x for x in array if x < pivot]
    equals = [x for x in array if x == pivot]
    bigger = [x for x in array if x > pivot]
    return random_pivot_quicksort(lesser) + equals + random_pivot_quicksort(bigger)

# I demonstrated same example to understand the working of two different logics
array = [10, 13, 15, 17, 8, 9, 1]
Output_sorted = random_pivot_quicksort(array)
print(Output_sorted)


#Output
#C:\Users\OMER\Desktop\DAA codes>C:/Python311/python.exe "c:/Users/OMER/Desktop/DAA codes/quicksort_random.py"
#[1, 8, 9, 10, 13, 15, 17]
