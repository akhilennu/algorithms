from Heap import MaxHeap

# O(NlogN)


def heapSort(Arr):

    Arr.append(Arr[0])
    N = len(Arr)
    print(N)
    obj = MaxHeap()
    heapSize = N-1
    obj.buildMaxHeap(Arr, heapSize)
    print("After build:", Arr)
    for i in range(N-1, 0, -1):
        Arr[1], Arr[i] = Arr[i], Arr[1]
        heapSize -= 1
        obj.maxHeapify(Arr, 1, heapSize)
        # print(Arr)
    return Arr[1:]


Arr = [50, 80, 95, 61, 57, 82, 30, 70, 67,
       2, 23, 81, 83, 65, 6, 76, 17, 15, 71, 13]
print("Before:", Arr)
ret = heapSort(Arr)
print("After:", ret)
