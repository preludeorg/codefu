# Why best?
#   Doesn't break SOLID (S)
#   Classes are discrete, strategy pattern applied
#   New sorts == new concrete strategy

import json
from abc import ABC, abstractmethod


class Best:
    def __init__(self, data):
        self.data = data

    def sort(self, strategy):
        return strategy.sort(self.data)


class SortingStrategy(ABC):
    @staticmethod
    @abstractmethod
    def sort(data):
        raise "Not implemented"


class BubbleSortConcreteStrategy(SortingStrategy):
    @staticmethod
    def sort(data):
        for n in range(len(data) - 1, 0, -1):
            for i in range(n):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
        return data


class InsertionSortConcreteStrategy(SortingStrategy):
    @staticmethod
    def sort(data):
        for i in range(1, len(data)):
            key_item = data[i]
            j = i - 1
            while j >= 0 and data[j] > key_item:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key_item
        return data


class PythonSortConcreteStrategy(SortingStrategy):
    @staticmethod
    def sort(data):
        return data.sort()


class Printer:

    def __init__(self, data):
        self.data = data

    def text(self):
        print(self.data)

    def json(self):
        print(json.dumps(self.data))


if __name__ == "__main__":
    best = Best([24, 56, 356, 346, 87, 56, 451, 7, 4, 7, 62, 513, 56, 5])
    printer = Printer(best.sort(BubbleSortConcreteStrategy()))
    printer.text()
    printer.json()
