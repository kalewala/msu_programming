"""
Программа параллельной сортировки

Python 3.10.7
"""

import numpy as np
import os
#from threading import Thread


# функция сортировки слиянием
def merge_sort(arr) -> np.ndarray:
    """Сортировка слиянием для np.ndarray
    
    Parameters
    ----------
    arr (np.ndarray): массив для сортировки

    Returns
    -------
    merge_lists (np.ndarray): отсортированный массив
    """

    
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


def file_div(file_name, parts=4):
    """Функция деления файла на части

    Parameters
    ----------
    file_name (str): путь к файлу
    parts (int): количество частей

    Returns
    -------
    int:
    """
    
    stats = os.stat(file_name)  # размер файла
    print("Исходный файл", stats.st_size)  # 128 байт отводится под метаданные
    size = stats.st_size - 128  # размер данных в файле
    print("Размер данных", size)
    #  определение точки остановки при чтении части файла
    if size % parts == 0:
        stop = size // parts
    else:
        stop = size // parts + 1
    print(stop)
    # цикл
        # чтение части файла
        # запись части файла
    pass


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

file_div(file_name)