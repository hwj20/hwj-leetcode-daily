'''
2028
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.
'''

'''

'''

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rem = mean*(n+len(rolls))-sum(rolls)
        mx_val = (6)*n
        mi_val = (1)*n
        # print(rem,mx_val,mi_val)
        if rem > mx_val or rem < mi_val:
            return []
        ans = []
        for i in range(n):
            if rem - (n-i-1) > 0:
                now = min(6,rem-(n-i-1))
                rem -=  now
                ans.append(now)
            else:
                ans.append(1)
        return ans

        
        