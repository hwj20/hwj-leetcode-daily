'''
1052
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.
'''

'''
好长的题目，
总之说是求，max(i in range(minute) sum(arr[i]xor grupy[i]))
前缀和完事
'''

class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(grumpy)
        s = [0]*n
        s[0] = grumpy[0] * customers[0]
        tot = 0
        if grumpy[0] == 0:
            tot += customers[0]
        for i in range(1,n):
            s[i] = grumpy[i] * customers[i]+s[i-1]
            if grumpy[i] == 0:
               tot += customers[i]
        mx = s[minutes-1]
        for i in range(minutes-1,n):
            mx = max(mx,s[i]-s[i-minutes])
        # print(s)
        # print(tot)
        return tot+mx