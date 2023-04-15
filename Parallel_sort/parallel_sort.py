"""
Программа параллельной сортировки
(на примере 2-ядерного процессора)

Python 3.10.7
"""

import numpy as np
import os
#from threading import Thread


# функция сортировки слиянием
def merge_sort(arr: np.ndarray) -> np.ndarray:
    """Сортировка слиянием для np.ndarray
    
    Parameter
    ----------
    arr (np.ndarray): массив для сортировки

    Return
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


# функция деления файла на части
def file_div(file_name: str, n: int) -> int:
    """Функция деления файла на части

    Parameters
    ----------
    file_name (str): путь к файлу
    n (int): количество байт для загрузки в оперативную память
    
    Return
    -------
    parts (int): количество частей файла
    """

    stats = os.stat(file_name)  # размер файла
    size = stats.st_size  # размер данных в файле

    #  определение количества частей файла
    if size % n == 0:
        parts = size // n
    else:
        parts = size // n + 1
    
    # чтение файла по частям и запись частей в отдельные файлы
    with open(file_name, "rb") as f:
        for i in range(1, parts + 1):
            data = f.read(n)
            with open(f"{file_name[:-4]}_{i}.bin", 'wb') as pf:
                pf.write(data)
    
    # вывод информации о результате
    print(f"Путь: {file_name}")
    print(f"Размер файла: {size} байт")
    print(f"Количество частей: {parts}")
    print(f"Размер части: {n} байт")
    return parts


def main():
    file_name = input("Имя файла (путь): ")  # имя файла для сортировки
    n = int(input("Количество чисел int32 для загрузки в оперативную память: "))
    file_name = "Parallel_sort/input.bin"
    n = 32

    n *= 4  # количество байт для загрузки в опертивную память
    parts = file_div(file_name, n)  # деление файла на части
    
    # сортировка частей
    for i in range(1, parts + 1):
        arr = np.fromfile(f"{file_name[:-4]}_{i}.bin", dtype=np.int32)  # чтение массива из части
        arr = merge_sort(arr)  # сортировка
        print(i, arr)

        # запист отсортированной части
        with open(f"Parallel_sort/output_{i}.bin", 'wb') as f:
            f.write(arr)


if __name__ == '__main__':
    main()