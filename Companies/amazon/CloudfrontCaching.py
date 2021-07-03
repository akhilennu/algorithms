import math

#
#


def connectedSum(n, edges):
    # Write your code here
    l = []
    l.append(set())
    for e in edges:
        for i in range(len(l)):
            tmp = set(e)
            s = l[i]
            k = len(s)
            m = s.union(tmp)
            print(l)
            if(len(m)-len(s) == 2):  # nothing in common
                l.append(tmp)
            else:
                l.pop(i)
                l.append(m)
    nodes_covered = 0
    sol = 0
    print(l)
    for s in l:
        tmp = len(s)
        nodes_covered += tmp
        sol += math.ceil(math.sqrt(tmp))
    sol += (n-nodes_covered)
    return sol


a = connectedSum(4, [[1, 2], [1, 4]])
print(a)
