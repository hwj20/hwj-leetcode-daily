'''
2392
You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.
'''

'''
看不懂题目捏，终于看懂了，有点像图论；提示说可以拓扑排序，逝逝二维拓扑排序;试完了，还是一维好点...
'''


def find_order(pairs, k):
    # 初始化图和入度表
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(1, k+1)}
    
    # 构建图和入度表
    for p in pairs:
        a,b = p[0],p[1]
        graph[a].append(b)
        in_degree[b] += 1
    
    # 找到所有入度为 0 的节点
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        # 将相邻节点的入度减 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 检查是否所有节点都在排序结果中
    if len(order) == k:
        return order
    else:
        return None


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        r_order = find_order(rowConditions,k)
        c_order = find_order(colConditions,k)
        # print(r_order,c_order)
        # from collections import defaultdict,deque
        # count = [0]*k
        if r_order == None or c_order == None:
            return [] 
        res = [[0]*k for _ in range(k)]
        for i in range(len(r_order)):
            for j in range(len(c_order)):
                if r_order[i] == c_order[j]:
                    res[i][j] = r_order[i] 
        return res
