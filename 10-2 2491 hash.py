'''
2491
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
'''

'''
cooking, need for speed
'''

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        target = sum(skill)/(n/2)
        m = {}
        ans = 0
        for s in skill:
            if s > target:
                return -1
            t = target-s
            if t in m and m[t] > 0:
                m[t] -= 1
                ans += t*s
            elif s not in m:
                m[s] = 1
            else:
                m[s] += 1
        for k in m:
            if m[k] > 0:
                return -1
        return int(ans)
                