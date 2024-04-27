'''
514. Freedom Trail
Hard
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
'''

'''
动规
难度主要在调试这里，眼睛都要看瞎了
'''



class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        from collections import defaultdict
        n = len(ring)
        ans = [[]*n]
        pos  = defaultdict(list)
        for i in range(n):
            pos[ring[i]].append(i)
        now = [(0,0)]    # (pos,ans)
        for c in key:
            # print(now)
            new_state = []
            for i in pos[c]:
                m = float('inf')
                res = []
                for state in now:
                    # print(abs(i-state[0])+1, n-abs(i-state[0])+1)
                    # print('-'*10)
                    # print(res)
                    if m > state[1]+min(+abs(i-state[0])+1, n-abs(i-state[0])+1):
                        m = state[1]+min(+abs(i-state[0])+1, n-abs(i-state[0])+1)
                        res = [(i,m)]
                    # elif m == min(abs(i-state[0])+1, n-abs(i-state[0])+1):
                    #     res.append((i,m+state[1]))
                new_state += res
            now = new_state
        # print(now)
        return min([x[1] for x in now])