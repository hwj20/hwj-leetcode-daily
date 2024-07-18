'''
1530
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.
'''

'''
每一层返回一个counter统计深度
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        global ans
        ans = 0
        def dfs(now):
            global ans
            if now == None:
                return {}
            res = {}
            l = dfs(now.left)
            r = dfs(now.right)
            for k,v in l.items():
                res[k+1] = v
                for d in range(2,distance+1):
                    if k<d and d-k in r:
                        ans += v*r[d-k]
            for k,v in r.items():
                if k+1 not in res:
                    res[k+1] = v
                else:
                    res[k+1] += v
            # print(now.val,res,l,r)
            if now.left == None and now.right == None:
                res[1] = 1 
            return res
        dfs(root)
        return ans

