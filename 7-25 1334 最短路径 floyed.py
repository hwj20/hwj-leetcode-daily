'''
1334
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
'''


'''
长得像bfs，实际上用个最短路径算法就是了（floyed）
'''
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')]*n for _ in range(n)]
        mx,ans = 105,-1
        for z in range(n):
            dis[z][z] = 0

        # edges.sort(key=lambda x:-x[2])
        for e in edges:
            a,b,w = e[0],e[1],e[2]
            dis[a][b] = dis[b][a] = min(dis[a][b],w)
        for z in range(n):
            for a in range(n):
                for b in range(n):
                    dis[a][b] = min(dis[a][b],dis[a][z]+dis[z][b])
        #         for z in range(n):
        #             if dis[a][z] != -1 and (dis[b][z] == -1 or w+dis[a][z] < dis[b][z]):
        #                 dis[z][b] = dis[b][z] = w+dis[a][z]
        #         for z in range(n):
        #             if dis[b][z] != -1 and (dis[a][z] == -1 or w+dis[b][z] < dis[a][z]):
        #                 dis[z][a] = dis[a][z] = w+dis[b][z]
        for i in range(n):
            r = 0
            for d in dis[i]:
                if d <= distanceThreshold:
                    r += 1
            # print(r,i)
            if  r <= mx:
                mx = r
                ans = i
        return ans
