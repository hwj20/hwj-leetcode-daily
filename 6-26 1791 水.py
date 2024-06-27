'''
1791
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
'''

'''
简单题，水一下
'''


class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        app = []
        for a,b in edges[:2]:
            if a not in app:
                app.append(a)
            else:
                return a
            if b not in app:
                app.append(b)
            else:
                return b
        