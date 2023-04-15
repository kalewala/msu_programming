"""
Генератор бинарного файла 32-битных целых чисел

Python 3.10.7
    numpy 1.23.4
"""

import numpy as np


# случайный массив int32
arr = np.random.randint(-2147483648,
                        high=2147483647,
                        size=128,
                        dtype="int32")

# запись бинарного файла
arr.tofile("Parallel_sort/input.bin")
