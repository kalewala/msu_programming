"""
Программа параллельной сортировки

Python 3.10.7
"""

import numpy as np
from threading import Thread


# функция сортировки слиянием
def merge_sort(arr):
    
    def merge_lists(left, right):
        i, j = 0, 0
        sort_list = np.array([], dtype="int32")
        while left.shape[0] > i and right.shape[0] > j:
            if left[i] < right[j]:
                sort_list = np.append(sort_list, left[i])
                i += 1
            else:
                sort_list = np.append(sort_list, right[j])
                j += 1
        if left.shape[0] > i:
            sort_list = np.append(sort_list, left[i:])
        if right.shape[0] > j:
            sort_list = np.append(sort_list, right[j:])
        return sort_list
    
    if arr.shape[0] == 1:
        return arr
    middle = arr.shape[0] // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge_lists(left, right)


# принимаемые параметры
#file_name = input()  # имя файла для сортировки
#n = int(input())  # количество чисел из файла для загрузки в память

file_name = "Parallel_sort/input.npy"

# открытие бинарного файла
lst = np.load("Parallel_sort/input.npy")


print("Input", lst)
#lst = list(lst)
#lst = merge_sort(lst)
print("Sorted", merge_sort(lst))