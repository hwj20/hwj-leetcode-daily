'''
826 Most Profit Assigning Work

You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.
'''


'''
需要选择某个难度下profit 最高的的答案
difficuty < 1e5 可以直接保存

'''


class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        tasks = [(difficulty[i],profit[i]) for i in range(len(profit))]
        tasks.sort()
        m = [0]*int(1e5+1)
        idx = 0
        for i in range(1,int(1e5+1)):
            if idx >= len(tasks) or i < tasks[idx][0]:
                m[i] = m[i-1]
            else:
                while idx < len(tasks) and tasks[idx][0] == i:
                    m[i] = max(m[i-1],tasks[idx][1])
                    idx += 1
        # print([m[w] for w in worker])
        ans = sum(m[w] for w in worker)
        return ans
        