'''
2045
A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.
'''

'''
题目说，这个图有个交通灯，也就是每过change minutes时间，你就得等change mins.
要求你返回第二小的返回时间

首先，时间是和路径长度成正比的，求出最短路径长度，就是最短时间；同理求出第二短路径(+1或者+2条边即可)

越写越烦...
'''

def calculate_total_time(n, time, change):
    # 初始化总时间
    total_time = 0
    
    for i in range(n):
        # 到达下一个节点所需的时间
        total_time += time
        # print(total_time)
        
        # 检查是否需要等待红绿灯
        if (total_time // change) % 2 == 1:
            # 如果总时间整除change的结果为奇数，说明是红灯
            # 计算需要等待的时间
            wait_time = change - (total_time % change)
            if i != n-1:
                total_time += wait_time
    
    return total_time

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:


        def dfs(now, depth,max_depth,f):
            # global n
            # print(now,depth)
            # vis.add(now)
            if depth == max_depth:
                return now == n
            if now == n:
                return False
            for d in e_map[now]:
                if d != f:
                    if dfs(d,depth+1,max_depth,now):
                        return True
            return False

        cnt = 0     
        q = deque([([],1)])


        target = -1
        last_depth = set()

        # while q:
        #     node = q.popleft()
        #     if len(node[0]) > dep:
        #         dep = len(node[0])
        #     for d in e_map[node[1]]:
        #         if d not in vis:
        #             vis.add(d)
        #             n_path = copy.deepcopy(node[0])
        #             q.append((,d))
        #         else:
        #             if d in last_depth
                    # 如果d在last_depth里面，说明有+1路
                    # 只要最短路径上存在任何+1路
        now_q = [(-1,1)] # father now
        next_q = []
        dep = 0
        # mt= [[False]*(n+1) for _ in range(n+1)]
        goodnode = [False]*(n+1)
        vis = set()
        vis.add(1)
        bad = set()
        from collections import defaultdict
        import heapq
        e_map = defaultdict(set)
        for e in edges:
            e_map[e[0]].add(e[1])
            e_map[e[1]].add(e[0])
            # mt[e[0]][e[1]] = mt[e[1]][e[0]] = True

        while now_q:
            # print(now_q)
            found_n = False
            bad.clear()
            v = []
            for f,now in now_q:
                goodnode[now] = goodnode[now] or goodnode[f]
                bad.add(now)
                if now == n:
                    found_n = True
                for t in e_map[now]:
                    # goodnode[t] = goodnode[t] or goodnode[now]
                    if t in bad:
                        goodnode[t] = goodnode[now] = True
                    if t not in vis:
                        v.append(t)
                        next_q.append((now,t))
                # print(goodnode)
            vis.update(v)
                # for _,t1 in next_q:
                #     for _,t2 in next_q:
                #         if mt[t1][t2]:
                #             goodnode[t1] = goodnode[t2] = True 
            dep += 1
            now_q = next_q
            next_q = []
            # print(found)
            if found_n:
                if goodnode[n]:
                    return calculate_total_time(dep, time, change)
                else:
                    return calculate_total_time(dep+1, time, change)
        return -1


