'''
860
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
'''

'''
stack
'''


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        from collections import defaultdict
        c = defaultdict(int)
        for bill in bills:
            if bill == 5:
                c[5] += 1
                continue
            if bill == 10:
                if c[5] > 0:
                    c[5] -= 1
                    c[10] += 1
                    continue
                else:
                    return False
            if bill == 20:
                if c[10] > 0 and c[5] > 0:
                    c[10] -= 1
                    c[5] -= 1
                    continue
                elif c[5] > 2:
                    c[5] -= 3
                    continue
                else:
                    return False
        return True