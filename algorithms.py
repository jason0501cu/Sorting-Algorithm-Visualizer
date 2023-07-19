class Algorithm:
    def __init__(self):
        self.algo_name = "Bubble Sort"
        self.algo_function = self.bubble_sort

    def bubble_sort(self, lst, ascending=True):
        is_sorted = False
        count = 0

        while not is_sorted:
            is_sorted = True

            for i in range(len(lst) - 1 - count):
                j = i + 1
                if (lst[i] > lst[j] and ascending) or (lst[i] < lst[j] and not ascending):
                    self._swap(i, j, lst)
                    is_sorted = False
                    yield i, j
            count += 1

    def insertion_sort(self, lst, ascending=True):
        for i in range(1, len(lst)):
            j = i

            
            while j > 0:
                sorting_cond = lst[j] < lst[j - 1] if ascending else lst[j] > lst[j - 1]
                if not sorting_cond:
                    break
                self._swap(j, j - 1, lst)
                j -= 1
                yield j + 1, j + 2

    def _swap(self, i, j, lst):
        lst[i], lst[j] = lst[j], lst[i]

    def change_function(self, name, func):
        self.algo_name = name
        self.algo_function = func
