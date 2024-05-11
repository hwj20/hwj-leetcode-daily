'''
857. Minimum Cost to Hire K Workers
Hard
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

Every worker in the paid group must be paid at least their minimum wage expectation.
In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.
'''

'''
没啥头绪，相当于对于一个确定的人来说，选了他，同时也选了工资倍率，看数量级最多是n^2的算法
萎靡了，直接看答案吧https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solutions/5141616/sorting-priority-max-heap-intuition
'''


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        n, cost = len(quality), float("inf")
        wq_ratio = [(float(w) / q, q) for w, q in zip(wage, quality)]
        total_q, q_heap = 0, []

        wq_ratio.sort(key=lambda x: x[0])
        for wq, q in wq_ratio:
            total_q += q
            heappush(q_heap, -q)

            if len(q_heap) > k:
                total_q += heappop(q_heap)
            
            if len(q_heap) == k:
                cost = min(cost, total_q * wq)

        return cost