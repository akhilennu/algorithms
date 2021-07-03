# Implementing max-heap
# https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/tutorial/

class MaxHeap:

    # Takes array and index and length(N)
    # if element in current index is not the higher than its children
    # it will swap with the highest child and repeat

    def maxHeapify(self, Arr, index, N):
        left = index*2
        right = index*2 + 1
        maximum = index
        if(left < N and Arr[left] > Arr[index]):
            maximum = left
        # I have compared with index earlier, be careful here. Compare right and maximum of left and index
        if(right < N and Arr[right] > Arr[maximum]):
            maximum = right
        if(maximum != index):
            Arr[index], Arr[maximum] = Arr[maximum], Arr[index]
            self.maxHeapify(Arr, maximum, N)

    # Runs max heapify on all nodes that are not leaf nodes
    def buildMaxHeap(self, Arr, N):
        for i in range((N//2), 0, -1):
            self.maxHeapify(Arr, i, N)
