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
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

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
                result += self.tree[l]
                l += 1
            if not (r & 1):
                result += self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
        return result

# Example usage:
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(data)
    print("Sum of range [1, 4]:", seg_tree.query(1, 4))
    seg_tree.update(2, 10)
    print("Updated sum of range [1, 4]:", seg_tree.query(1, 4))
