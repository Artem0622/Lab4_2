#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Hex для работы с беззнаковыми целыми шестнадцатеричными числами,
используя для представления числа список из 100 элементов типа int, каждый из которых
является шестнадцатеричной цифрой. Младшая цифра имеет меньший индекс. Реальный
размер списка задается как аргумент конструктора инициализации. Реализовать
арифметические операции, аналогичные встроенным для целых и операции сравнения.
"""


class Hex:
    SIZE_LIMIT = 100  # Максимальный размер списка

    def __init__(self, value=0):
        self.count = 0
        self.digits = [0] * self.SIZE_LIMIT
        self.set_value(value)

    def set_value(self, value):
        hex_str = hex(value)[2:].upper()
        self.count = min(len(hex_str), self.SIZE_LIMIT)
        self.digits[:self.count] = [int(d, 16) for d in hex_str[-self.count:][::-1]]

    def get_size(self):
        return self.SIZE_LIMIT

    def __getitem__(self, index):
        if 0 <= index < self.SIZE_LIMIT:
            return self.digits[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self.SIZE_LIMIT:
            self.digits[index] = value
        else:
            raise IndexError("Index out of range")

    def display(self):
        print("0x" + "".join([hex(d)[2:].upper() for d in self.digits[::-1]]))


if __name__ == "__main__":
    hex_num = Hex(255)
    hex_num.display()

    print("Size:", hex_num.get_size())
    print("Element at index 2:", hex_num[2])

    hex_num[1] = 10
    hex_num.display()
