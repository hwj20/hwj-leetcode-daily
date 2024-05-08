'''
506. Relative Ranks
Easy
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.
'''



'''
怪可爱的题目，我是不是写复杂了？
'''



class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        dic = {1:"Gold Medal",2:"Silver Medal",3:"Bronze Medal"}
        score = sorted([(score[i],i) for i in range(len(score))],key=lambda x:-x[0])
        res = [0]*len(score)
        for i in range(len(score)):
            p = score[i][1]
            if i+1 in dic:
                res[p] = dic[i+1]
            else:
                res[p] = str(i+1)
        return res