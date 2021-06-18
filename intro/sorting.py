l = [50,  80,  95,  61,  57,  82,  30,  70,  67,   2,
     23,  81,  83,  65,   6,  76,  17,  15,  71,  13,  25]


def selectionSort(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if(l[i] > l[j]):
                l[i], l[j] = l[j], l[i]
    return l


def quicksort(l):
    if(len(l) < 2):
        return l
    pivot = l[0]
    # <= to handle if the pivot number is duplicate.
    # Since we're looping on array excluding 1st element we wont get the pivot here
    less = [i for i in l[1:] if i <= pivot]
    greater = [i for i in l[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort(l))
