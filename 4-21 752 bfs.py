'''
752. Open the Lock
Medium

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
'''

'''
经典bfs题，但为什么我的BFS t掉了或者时间很紧啊，想不通。
家人们，我控制了下变量，如果把deadends变成set，就能减少2/3的时间，太牛批了。
'''


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        def findstates(s):
            res = []
            for i in range(4):
                s1 = s[:i]+str((int(s[i])+1)%10)+s[i+1:]
                if (s1 not in vis) and s1 not in deadends:
                    res.append(s1)  
                s2 = s[:i]+str((int(s[i])-1)%10)+s[i+1:]  
                if (s2 not in vis) and s2 not in deadends:          
                    res.append(s2)
            # print(res)
            return res

        q = deque([('0000',0)])
        vis = set('0000')
        deadends = set(deadends)
        if target == '0000':
            return 0
        if '0000' in deadends:
            return -1
        while q:
            node = q.popleft()
            now,p = node[0],node[1]
            # 注意，不能在这里加
            # vis.add(now)
            states = findstates(now)
            for state in states:
                if state == target:
                    return p+1
                q.append((state,p+1))
                vis.add(state)
            # print(q)
        return -1