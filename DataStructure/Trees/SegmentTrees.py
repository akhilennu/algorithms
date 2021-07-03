class SegmentTree:
    def __init__(self, arr) -> None:
        self.tree = [0]*len(arr)*2
        self.arr = arr

    #
    #   Prepare the binary tree such that top node will be sum of all nodes
    #  #
    def build_tree(self, node, start, end):
        if(start == end):
            self.tree[node] = self.arr[start]
        else:
            mid = (start+end)//2
            self.build_tree(node*2, start, mid)
            self.build_tree(node*2+1, mid+1, end)
            self.tree[node] = self.tree[node*2]+self.tree[node*2+1]

    #
    #  Update the value at index and the tree
    # #
    def update(self, node, start, end, index, value):
        if(start == end):
            self.tree[node] = value
            self.arr[start] = value
        else:
            mid = (start+end)//2
            if(start <= index <= mid):
                self.update(node*2, start, mid, index, value)
            else:
                self.update(node*2+1, mid+1, end, index, value)
            self.tree[node] = self.tree[node*2]+self.tree[node*2+1]

    #
    # Query to findout sum of all nodes between left and right
    # #
    def query(self, node, start, end, left, right):
        # print(start, end)
        if(end < left or start > right):
            return 0
        elif(left <= start and end <= right):  # start and end between left and right
            print("returning ", self.tree[node], " at ", start, end)
            return self.tree[node]
        else:
            mid = (start+end)//2
            return self.query(node*2, start, mid, left, right) + self.query(node*2+1, mid+1, end, left, right)


arr = [1, 2, 3, 4, 5, 6, 7, 8]
obj = SegmentTree(arr)
start = 0
end = len(arr)-1
obj.build_tree(1, start, end)
print("after build:", obj.tree)

obj.update(1, start, end, 6, 11)
print("after update:", obj.tree)

sol = obj.query(1, start, end, 3, 5)
print(sol)
