'''
2751
Hard
There are n 1-indexed robots, each having a position on a line, health, and movement direction.

You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.
'''

'''
一个位置在p的机器人，假如方向为L，那么它受到的伤害等于min(health, max(左边所有R-左边所有L,0))；
题目看错了哈哈哈，看成减所有值了，实际是减一;
考虑 stack，维持一个L_stack每次有右边的就减一
'''
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        s_p = {v:p for p,v in enumerate (sorted(positions))}
        positions = [s_p[k] for k in positions]
        n = len(positions)
        r_map = {v:k for k,v in enumerate(positions)}
        # ll,lr,rr,rl = [0]*(n+1),[0]*(n+1),[0]*(n+1),[0]*(n+1)
        # print(positions,r_map)
        # for i in range(n):
        #     if directions[r_map[i]] == 'L':
        #         ll[i+1] = ll[i]+healths[r_map[i]]
        #         lr[i+1] = lr[i]
        #     else:
        #         ll[i+1] = ll[i]
        #         lr[i+1] = lr[i]+healths[r_map[i]]
        # for i in range(n,0,-1):
        #     print(i)
        #     if directions[r_map[i-1]] == 'L':
        #         rl[i-1] = rl[i]+healths[r_map[i-1]]
        #         rr[i-1] = rr[i]
        #     else:
        #         rl[i-1] = rl[i]
        #         rr[i-1] = rr[i]+healths[r_map[i-1]]
        # for i in range(n):
        #     if directions[r_map[i]] == 'L':
        #         healths[r_map[i]] -= min(healths[r_map[i]],max(lr[i]-ll[i],0))
        #     else:
        #         healths[r_map[i]] -= min(healths[r_map[i]],max(rl[i]-rr[i+1],0))
        # return list(filter(lambda x:x!=0,healths))
        s = []
        for i in range(n):
            # print(s)
            if directions[r_map[i]] == 'R':
                s.append(r_map[i])
            else:
                while s and healths[s[-1]] < healths[r_map[i]]:
                    healths[s[-1]] = 0
                    s.pop()
                    healths[r_map[i]] -= 1
                if healths[r_map[i]] != 0 and s:
                    if healths[r_map[i]] == healths[s[-1]]:
                        healths[s[-1]] = 0
                        s.pop()
                        healths[r_map[i]] = 0
                    else:
                        healths[r_map[i]] = 0
                        healths[s[-1]] -= 1

            
        return list(filter(lambda x:x!=0,healths))                
                     
