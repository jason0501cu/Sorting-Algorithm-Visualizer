class Algorithm:
    def __init__(self):
        self.algo_name = "Bubble Sort"
        self.algo_function = self.bubble_sort
    
    def bubble_sort(self, lst, ascending=True):
        is_sorted = False
        end = len(lst) - 1

        while not is_sorted:
            is_sorted = True
            
            for i in range(end):
                j = i + 1
                if (lst[i] > lst[j] and ascending) or (lst[i] < lst[j] and not ascending):
                    self._swap(i, j, lst)
                    is_sorted = False
                    yield i, j


    def _swap(self, i, j, lst):
        lst[i], lst[j] = lst[j], lst[i]