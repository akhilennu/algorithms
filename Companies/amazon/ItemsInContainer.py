

# 1. Initialize a hashmap
# 2. Store all the container index as key and number of containers until that index as Value
# 3. Find the nearest container from left and nearest container from right
# 4. Number of containers at right index - number of containers at left index = number of containers in between
# 5. Number of stars is right index - left index - number of containers in between
# 6. Recheck the question if we have to count * from startIndex till endIndex or
#     from the first container after start index till the last container before end index.

# This is not the solution applied below

def numOfItems(s, startIndex, endIndex):
    i = startIndex-1
    j = i+1
    sol = 0
    while(j < len(s) and j < endIndex):
        while(s[i] != '|'):
            i += 1
            j += 1
        if(j < len(s) and j < endIndex and s[j] == '|'):
            # print(i, j)
            sol += j-i-1
            i = j
        j += 1
    return sol


def numberOfItems(s: str, startIndices, endIndices):
    indicesLen = len(startIndices)
    sol = []
    for i in range(indicesLen):
        sol.append(numOfItems(s, startIndices[i], endIndices[i]))
    return sol


s = "*|**|"

a = numberOfItems(s, [1, 2], [3, 5])
print(a)
