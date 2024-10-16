'''
1405
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.
'''

'''
heap
'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = [(a,'a'),(b,'b'),(c,'c')]
        ans = ""
        while True:
            mx = max(d)
            d.remove(mx)
            if mx[0] == 0:
                return ans
            if len(ans) < 2 or ans[-1] != ans[-2]:
                ans+= mx[1]
                nmx = (mx[0]-1,mx[1])
                # mx[0] -= 1
                d.append(nmx)
            elif ans[-1] == mx[1]:
                mx2 = max(d)
                d.append(mx)
                d.remove(mx2)
                if mx2[0] == 0:
                    return ans
                ans += mx2[1]
                nmx2 = (mx2[0]-1,mx2[1])
                d.append(nmx2)
            else:
                ans+= mx[1]
                nmx = (mx[0]-1,mx[1])
                # mx[0] -= 1
                d.append(nmx)               
            # print(ans,d)
