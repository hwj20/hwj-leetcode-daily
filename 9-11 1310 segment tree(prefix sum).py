'''
1310
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.
'''

'''
segment tree?
'''

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        # Build the segment tree
        self.build(data)

    def build(self, data):
        # Insert leaf nodes in the tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] ^ self.tree[i << 1 | 1]

    def update(self, pos, value):
        # Change the index to the leaf node
        pos += self.n
        self.tree[pos] = value
        # Move up in the tree and update parents
        i = pos
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def query(self, l, r):
        # Range sum query from index l to r
        l += self.n
        r += self.n
        result = 0
        while l <= r:
            if (l & 1):
                result = result ^ self.tree[l]
                l += 1
            if not (r & 1):
                result ^= self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return result

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        tree = SegmentTree(arr)
        res = []
        for a,b in queries:
            res.append(tree.query(a,b))
        return res