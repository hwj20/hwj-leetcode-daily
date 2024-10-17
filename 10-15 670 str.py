'''
670
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        idx = -1
        now = -1
        temp = str(num)
        base = ""
        for i in range(len(temp)):
            idx = -1
            now = int(temp[i])
            for j in range(i+1,len(temp)):
                if int(temp[j]) > now:
                    now = int(temp[j])
                    idx = j
                    # print(now)
                elif int(temp[j]) == now and temp[j] != temp[i]:
                    idx = j
            # print(j)
            if idx != -1:
                return int(base+temp[idx]+temp[i+1:idx]+temp[i]+temp[idx+1:])
            base += temp[i]
        return int(base)
        