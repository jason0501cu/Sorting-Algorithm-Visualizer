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
                else:
                    self._swap(j, j - 1, lst)
                j -= 1
                yield j + 1, j + 2
    
    def selection_sort(self, lst, ascending=True):
        i = 0
        while i < len(lst) - 1:
            target_idx = i
            for idx in range(i + 1, len(lst)):
                sorting_cond = lst[target_idx] > lst[idx]if ascending else lst[target_idx] < lst[idx]
                if sorting_cond:
                    target_idx = idx
            self._swap(i, target_idx, lst)
            yield i, target_idx
            i += 1

    def heap_sort(self, lst, ascending=True):
        # To start the heap sort, a heap is first built. If the sorting is in ascending order, a max-heap is built,
        # while for descending order sorting, a min-heap is built.
        first_parent_idx = (len(lst) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
        # This block of code is the siftDown function, which adjusts the heap so that it maintains
        # its property of being a max-heap (for ascending order sorting) or min-heap (for descending order sorting).
            end_idx = len(lst) - 1
            child_one_idx = current_idx * 2 + 1
            while child_one_idx <= end_idx:
                child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
                if child_two_idx > -1 and ((ascending and lst[child_two_idx] > lst[child_one_idx]) or 
                                  (not ascending and lst[child_two_idx] < lst[child_one_idx])):
                    idx_to_swap = child_two_idx
                else:
                    idx_to_swap = child_one_idx
                if (ascending and lst[idx_to_swap] > lst[current_idx]) or \
                    (not ascending and lst[idx_to_swap] < lst[current_idx]):
                    self._swap(current_idx, idx_to_swap, lst)  # Swap the values at the current index and the swap index.
                    yield current_idx, idx_to_swap  # Generate a tuple of the current index and the swap index.
                    current_idx = idx_to_swap  # Set the current index to the swap index for the next iteration.
                    child_one_idx = current_idx * 2 + 1  # Recalculate the index of the first child node.
                else:
                    break

        # After the heap has been built, the heap sort starts.
        for end_idx in reversed(range(1, len(lst))):
            self._swap(0, end_idx, lst)  # Swap the root of the heap with the last node.
            yield 0, end_idx  # Generate a tuple of the root index (0) and the end index.
            # This block of code is the siftDown function, which ensures that the heap property is maintained
            # after the root and the last node have been swapped.
            current_idx = 0
            child_one_idx = current_idx * 2 + 1
            while child_one_idx <= end_idx - 1:
                child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx - 1 else -1
                if child_two_idx > -1 and ((ascending and lst[child_two_idx] > lst[child_one_idx]) or 
                                  (not ascending and lst[child_two_idx] < lst[child_one_idx])):
                    idx_to_swap = child_two_idx
                else:
                    idx_to_swap = child_one_idx
                if (ascending and lst[idx_to_swap] > lst[current_idx]) or \
                    (not ascending and lst[idx_to_swap] < lst[current_idx]):
                    self._swap(current_idx, idx_to_swap, lst)  # Swap the values at the current index and the swap index.
                    yield current_idx, idx_to_swap  # Generate a tuple of the current index and the swap index.
                    current_idx = idx_to_swap  # Set the current index to the swap index for the next iteration.
                    child_one_idx = current_idx * 2 + 1  # Recalculate the index of the first child node.
                else:
                    break


    def quick_sort(self, lst, ascending=True):
        stack = [(0, len(lst) - 1)]

        while stack:
            start_idx, end_idx = stack.pop()
            if start_idx >= end_idx:
                continue

            pivot_idx = lst[start_idx]
            low_idx = start_idx + 1
            high_idx = end_idx

            while True:
                if ascending:
                    while low_idx <= high_idx and lst[high_idx] >= pivot_idx:
                        high_idx -= 1
                    while low_idx <= high_idx and lst[low_idx] <= pivot_idx:
                        low_idx += 1
                else:
                    while low_idx <= high_idx and lst[high_idx] <= pivot_idx:
                        high_idx -= 1
                    while low_idx <= high_idx and lst[low_idx] >= pivot_idx:
                        low_idx += 1

                if low_idx <= high_idx:
                    self._swap(low_idx, high_idx, lst)
                    yield low_idx, high_idx
                else:
                    break
            self._swap(start_idx, high_idx,lst)
            yield start_idx, high_idx

            stack.extend(((start_idx, high_idx - 1), (high_idx + 1, end_idx)))
            



    def _swap(self, i, j, lst):
        lst[i], lst[j] = lst[j], lst[i]

    def change_function(self, name, func):
        self.algo_name = name
        self.algo_function = func
