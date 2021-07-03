# Takes array and index and length(N)
# if element in current index is not the higher than its children
# it will swap with the highest child and repeat

def maxHeapify(Arr, index, N):
    left = index*2
    right = index*2 + 1
    maximum = index
    if(left < N and Arr[left] > Arr[index]):
        maximum = left
    if(right < N and Arr[right] > Arr[maximum]):
        maximum = right
    if(maximum != index):
        Arr[index], Arr[maximum] = Arr[maximum], Arr[index]
        maxHeapify(Arr, maximum, N)

    # Runs max heapify on all nodes that are not leaf nodes


def buildMaxHeap(Arr, N):
    for i in range((N//2), 0, -1):
        maxHeapify(Arr, i, N)


def maximum(Arr):
    # return the maximum
    return Arr[1]


def extractMaximum(Arr):
    # pop the maximum and return it
    size = len(Arr)
    if(size < 2):
        return -1  # Heap is empty
    maximum = Arr[1]
    Arr[1] = Arr[size-1]
    Arr.pop(size-1)
    size = size - 1
    maxHeapify(Arr, 1, size)
    return maximum


def increase_val(Arr, i, val):
    # increase the value of item at index and adjust the heap
    if(val < Arr[i]):
        return  # Cannot decrease the value
    Arr[i] = val
    while(i > 1 and Arr[i//2] < Arr[i]):
        Arr[i//2], Arr[i] = Arr[i], Arr[i//2]
        i = i//2


def insert_val(Arr, val):
    # insert the value in heap
    Arr.append(-1)  # Assuming all numbers are positive
    N = len(Arr)
    return increase_val(Arr, N-1, val)


Arr = [7, 4, 8, 1, 3]

# Convert to heap
print("original :", Arr)
Arr.append(Arr[0])
N = len(Arr)
print("appended 0th item to nth pos:", Arr[1:])
buildMaxHeap(Arr, N)
print("after heapify:", Arr[1:])
print("Max is:", extractMaximum(Arr))

print("after extract:", Arr[1:])
print("Max is:", extractMaximum(Arr))
print("after extract:", Arr[1:])
insert_val(Arr, 5)
insert_val(Arr, 2)
print("after insert 5,2:", Arr[1:])
print("Max is:", extractMaximum(Arr))
print("after extract:", Arr[1:])
print("Max is:", extractMaximum(Arr))
print("after extract:", Arr[1:])
print("Max is:", extractMaximum(Arr))
print("after extract:", Arr[1:])
print("Max is:", extractMaximum(Arr))
print("after extract:", Arr[1:])
print("Max is:", extractMaximum(Arr))
print("after extract:", Arr[1:])
print("Max is:", extractMaximum(Arr))
print("after extract:", Arr[1:])
