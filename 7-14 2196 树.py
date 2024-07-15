'''
2196
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.
'''

'''
我这个代码怎么就只打败了20%的时间复杂度
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        m = {}
        n_root = set()
        for d in descriptions:
            if d[0] not in m:
                m[d[0]] = TreeNode(val=d[0])
            if d[1] not in m:
                m[d[1]] = TreeNode(val=d[1])
            n_root.add(d[1])
            if d[2] == 0:
                m[d[0]].right = m[d[1]]
            else:
                m[d[0]].left = m[d[1]]
        for k,_ in m.items():
            if k not in n_root:
                return m[k]
        return None