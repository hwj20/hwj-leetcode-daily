'''
874
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).

Note:

North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
There can be obstacle in [0,0].
'''

'''
sim
'''


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob = set([int(y*1e5+x) for x,y in obstacles])
        # ob.sort()
        global ans
        ans = 0
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        def mov(x,y,com,dr,cmd_idx):
            global ans
            ans = max(ans,x**2+y**2)
            if com == -1:
                dr += 1
                dr %= 4
                cmd_idx += 1
                if cmd_idx == len(commands):
                    return
                mov(x,y,commands[cmd_idx],dr,cmd_idx)
                return
            elif com == -2:
                dr -= 1
                dr %= 4
                cmd_idx += 1
                if cmd_idx == len(commands):
                    return
                mov(x,y,commands[cmd_idx],dr,cmd_idx)
                return
            if com == 0:
                cmd_idx += 1
                if cmd_idx == len(commands):
                    return
                mov(x,y,commands[cmd_idx],dr,cmd_idx)
                return
            # print(int(x*1e5+y))
            # if int(x*1e5+y) in ob:
            #     cmd_idx += 1
            #     if cmd_idx == len(commands):
            #         return
            #     mov(x,y,commands[cmd_idx],dr,cmd_idx)
            #     return
            dx,dy = dirs[dr]
            x += dx
            y += dy
            if int(x*1e5+y) not in ob:
                mov(x,y,com-1,dr,cmd_idx)
            else:
                x -= dx
                y -= dy
                cmd_idx += 1
                if cmd_idx == len(commands):
                    return
                mov(x,y,commands[cmd_idx],dr,cmd_idx)                
            return
        mov(0,0,0,0,-1)
        return ans
