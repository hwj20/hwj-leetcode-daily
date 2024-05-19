'''
3068. Find the Maximum Sum of Node Values
Hard
There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
nums[u] = nums[u] XOR k
nums[v] = nums[v] XOR k
Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.
'''

'''
对于每个点，有一个gain，当每条边被选后 gain 变成 -gain，而对于每条边一次操作的收益是 gain(u)+gain(v)，而连接的所有边的收益里的gain(u)会变成-gain(u)。
我们可以大胆猜测，当树里所有点都是负收益的时候，结果就是最优解，那我们能不能通过无数次操作把所有点的收益变成负的呢？不能，因为对于叶子节点来说，变成负收益的方法是一定的，这样一层一层地上去，我们会得到一个确定的图。同时，改变根节点也不会改变根节点的正负性
但是！我们能保证除了根节点全是负的图。也就是说，答案会是，sum(max(num,num XOR k))(如果根节点是正的) or sum(max(num,num XOR k)) - min((num XOR k)-num)
'''

class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        from collections import defaultdict
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        vis = set()
        e = defaultdict(list)
        for edge in edges:
            e[edge[0]].append(edge[1])
            e[edge[1]].append(edge[0])

        max_sum = [0]
        min_gain = [float('inf')]
        def dfs(now):
            vis.add(now)
            num = nums[now]
            gain = (num ^ k) -num
            positive = False # do operation
            if gain > 0:
                positive = True
                max_sum[0] += num ^ k
            else:
                max_sum[0] += num
            min_gain[0] = min(min_gain[0],abs(gain))
            for des in e[now]:
                if des not in vis:
                    positive = positive ^ dfs(des)
            return positive
        if dfs(0):
            return max_sum[0] - min_gain[0]
        else:
            return max_sum[0]