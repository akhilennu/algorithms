l = [50,  80,  95,  61,  57,  82,  30,  70,  67,   2,
     23,  81,  83,  65,   6,  76,  17,  15,  71,  13,  25]

l.sort()

print(l)


def binarySearch(lst: list, s: int):
    low = 0
    high = len(l)-1
    itercount = 0
    while(low <= high):
        mid = int((low+high)/2)
        guess = lst[mid]
        if(guess == s):
            print('Number of iterations', itercount)
            return mid
        elif(guess > s):
            high = mid - 1
        else:
            low = mid+1
        itercount += 1
    print('Number of iterations', itercount)
    return None


print(binarySearch(l, int(input('enter a number to search: '))))
