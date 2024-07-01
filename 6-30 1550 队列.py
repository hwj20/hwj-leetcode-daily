'''
1550. Three Consecutive Odds
iven an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
'''


class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool    
        """
        for i in range(len(arr)):
            s = 0
            for j in range(3):
                if i+j >= len(arr):
                    return False
                s += arr[i+j]%2
            if s == 3:
                return True
        return False
       