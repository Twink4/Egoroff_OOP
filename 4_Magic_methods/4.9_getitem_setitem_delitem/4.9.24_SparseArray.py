class SparseArray:

    def __init__(self, *args):
        self.__values = [*args]

    def __getitem__(self, index: int):
        self.__check_indexes(index)
        return self.__values[index]

    def __setitem__(self, index: int, value: int):
        self.__check_indexes(index)
        self.__values[index] = value

    def __check_indexes(self, index: int):
        if index > len(self.__values):
            self.__values.extend(None for _ in range(index - len(self.__values) + 1))

    def __delitem__(self, index: int):
        self.__values[index] = None

    def __len__(self):
        return len(self.__values)

    @property
    def values(self):
        return tuple(self.__values)


array = SparseArray(1, 2, 3)
print(array.values)
print(array[7])
print(array.values)
array[6] = 100
print(array.values)
array[10] = 200
print(array.values)
del array[1]
print(array.values)
print(len(array))

print()

array = SparseArray()
print(array.values)
array[5] = 4
array[0] = 13
array[10] = 23
array[5] = 81
array[7] = 100
print(array.values)
print(len(array))
print(array[20])
print(array.values)
