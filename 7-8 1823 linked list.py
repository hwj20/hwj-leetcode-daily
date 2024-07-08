'''
1823
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.
'''

'''
用一个circle list就很好解
'''

class Node:
    def __init__(self, val: int, nxt: 'Node' = None, prev: 'Node' = None):
        self.val = val
        self.next = nxt
        self.prev = prev


class CircleList:
    def __init__(self,l):
        self.head = Node(1,None)
        t = self.head
        for i in range(l-1):
            n = Node(i+2,None)
            n.prev = t
            t.next = n
            t = n
        self.head.prev = t
        t.next = self.head
    def is_end(self,now):
        return now.next == now
    def remove(self,m,now):
        last = now.prev
        for _ in range(m-1):
            last = now
            now = now.next
        now.next.prev = last
        last.next = now.next
        return now.next




class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        li = CircleList(n)
        now = li.head
        while not li.is_end(now):
            # print(now.val)
            now = li.remove(k,now)
        return now.val