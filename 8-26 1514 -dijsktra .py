'''
1514
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
'''

'''
dijstrak
'''
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        from collections import defaultdict
        e_map = defaultdict(list)
        for i in range(len(succProb)):
            a,b,val = edges[i][0],edges[i][1],succProb[i]
            e_map[a].append((b,val))
            e_map[b].append((a,val))
        ans = [0]*n
        ans[start_node] = 1
        import heapq
        hp = [(-ans[start_node],start_node)]
        while hp:
            # print(hp)
            res,node = heapq.heappop(hp)
            if node == end_node:
                return -res
            # res,node = hp.pop()
            res = -res
            if res < ans[node]:
                continue
            else:
                ans[node] = res
                for d,v in e_map[node]:
                    if res*v > ans[d]:
                        ans[d] = res*v
                        # hp.append((ans[d],d))
                        heapq.heappush(hp,(-ans[d],d))
    
        return ans[end_node]
