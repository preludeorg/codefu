# Why better?
#   Doesn't break SOLID (S)
#
# Why bad?
#   Class bloat
#   Changes to multiple locations in the code to add new sorts

import json


class Better:

    def __init__(self, sort):
        self.sort = sort

    def sort_data(self, data):
        if self.sort == 'bubble':
            return self._bubble_sort(data)
        elif self.sort == 'python':
            return self._python_sort(data)
        elif self.sort == 'insertion':
            return self._insertion_sort(data)

    @staticmethod
    def _bubble_sort(data):
        for n in range(len(data) - 1, 0, -1):
            for i in range(n):
                if data[i] > data[i + 1]:
                    # swapping data if the element is less than next element in the array
                    data[i], data[i + 1] = data[i + 1], data[i]
        return data

    @staticmethod
    def _python_sort(data):
        return data.sort()

    @staticmethod
    def _insertion_sort(data):
        for i in range(1, len(data)):
            key_item = data[i]
            j = i - 1
            while j >= 0 and data[j] > key_item:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key_item
        return data


class Printer:

    def __init__(self, data):
        self.data = data

    def text(self):
        print(self.data)

    def json(self):
        print(json.dumps(self.data))


if __name__ == "__main__":
    better = Better('bubble')
    printer = Printer(better.sort_data([24, 56, 356, 346, 87, 56, 451, 7, 4, 7, 62, 513, 56, 5]))
    printer.text()
    printer.json()
