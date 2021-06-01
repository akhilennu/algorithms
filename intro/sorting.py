l = [50,  80,  95,  61,  57,  82,  30,  70,  67,   2,
     23,  81,  83,  65,   6,  76,  17,  15,  71,  13,  25]


def selectionSort(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if(l[i] > l[j]):
                l[i], l[j] = l[j], l[i]
    print(l)


selectionSort(l)
