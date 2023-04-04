"""
Программа параллельной сортировки

Python 3.10.7
"""

# функция сортировки слиянием
def merge_sort(lst):
    
    def merge_lists(left, right):
        i, j = 0, 0
        sort_list = []
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                sort_list.append(left[i])
                i += 1
            else:
                sort_list.append(right[j])
                j += 1
        if len(left) > i:
            sort_list += left[i:]
        if len(right) > j:
            sort_list += right[j:]
        return sort_list
    
    if len(lst) == 1:
        return lst
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge_lists(left, right)


# принимаемые параметры
file_name = input()  # имя файла для сортировки
n = int(input())  # количество чисел из файла для загрузки в память