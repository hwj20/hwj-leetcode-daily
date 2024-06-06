'''
846. Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
'''

'''
肯定从小到大排列，因为每个最小的数，一定得删除后面n-consequential个
'''
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        from collections import Counter
        import copy
        hand.sort()
        count = Counter(hand)
        count2 = copy.deepcopy(count)
        i = 0
        while i < len(hand):
            if count[hand[i]] == 0:
                i += count2[hand[i]]
                continue
            start = hand[i]
            offset = count2[start]
            for j in range(1,groupSize):
                if i + offset >= len(hand):
                    return False
                now = hand[i+offset]
                if now != start+j:
                    return False
                offset += count2[now]
                count[now] -= count[start]
                if count[now] < 0:
                    return False
            i += count2[hand[i]]
        return True


