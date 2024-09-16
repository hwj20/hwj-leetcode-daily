'''
539
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
'''

'''
'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(s:str):
            h,m = (int(s.split(":")[0]),int(s.split(":")[1]))
            return h*60+m
        t = [convert(x) for x in timePoints]
        for i in range(len(t)):
            t.append(1440+t[i])
        t.sort()
        ans = float("inf")
        for i in range(len(t)-1):
            if t[i+1] == t[i]:
                return 0
            ans = min(ans,min(1440-(t[i+1]-t[i]),(t[i+1]-t[i])))
        return ans
            