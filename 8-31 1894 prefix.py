'''
1894
There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. After that, the teacher will restart the process, starting with the student number 0 again.

You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to replace the chalk.

Return the index of the student that will replace the chalk pieces.
'''

'''
prefix
'''

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        import copy
        prefix = copy.deepcopy(chalk)
        prefix.insert(0,0)
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        # print(prefix)
        k %= prefix[-1]
        for i in range(len(chalk)):
            if prefix[i+1] > k:
                return i
        return -1
