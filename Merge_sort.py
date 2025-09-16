####
import time

def join(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res + left[i:] + right[j:]

def merge_sort(ls):
    n = len(ls)
    if n <= 1:
        return ls
    mid = n//2
    left, right = merge_sort(ls[:mid]), merge_sort(ls[mid:])
    return join(left, right)

    

start_time = time.time()
print(merge_sort(list(range(101))+ [9, 2, 4, 5] * 25 + list(range(100, -1, -1))))
end_time = time.time()
print(end_time - start_time)