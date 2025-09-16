####
import time

def quick_sort(ls):
    low, high = 0, len(ls)-1

    def recursive_quick_sort(low, high):

        def partition(low, high):
            pivot_value = ls[high]
            i = low-1
            for j in range(low, high):
                if ls[j] < pivot_value:
                    i += 1
                    ls[i], ls[j] = ls[j], ls[i]
            ls[i+1], ls[high] = ls[high], ls[i+1]
            return i+1

        if low < high:
            pivot = partition(low, high)
            recursive_quick_sort(low, pivot-1)
            recursive_quick_sort(pivot+1, high)

    recursive_quick_sort(low, high)
    return ls

    
start_time = time.time()
print(quick_sort(list(range(101)) + [9, 2, 4, 5] * 25 + list(range(100, -1, -1))))
end_time = time.time()
print(end_time - start_time)