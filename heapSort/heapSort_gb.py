def heapsort(lst):
    build_max_heap(lst)
    for i in range(len(lst) - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        max_heapify(lst, index=0, size=i)


def build_max_heap(lst):
    start = ((len(lst) - 2) // 2)
    while start >= 0:
        max_heapify(lst, index=start, size=len(lst))
        start = start - 1


def max_heapify(lst, index, size):
    l = 2 * index + 1
    r = 2 * index + 2
    if (l < size and lst[l] > lst[index]):
        largest = l
    else:
        largest = index
    if (r < size and lst[r] > lst[largest]):
        largest = r
    if (largest != index):
        lst[largest], lst[index] = lst[index], lst[largest]
        max_heapify(lst, largest, size)


lst_1 = [int(input(f'Input the {i + 1} number: ')) for i in range(int(input('Input list length: ')))]
heapsort(lst_1)
print('Sorted list:\n{}'.format(lst_1))