'''
1518
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
'''

'''
有趣的问题
'''



class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans = 0
        water,empty = numBottles,0
        while (water+empty) >= numExchange:
            ans += water
            empty += water
            water = empty // numExchange
            empty -=  water*numExchange
        return ans+water