'''
2406
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.
'''


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for interval in intervals:
            left, right = interval
            events.append((left, 1))   # interval start
            events.append((right + 1, -1)) # interval end (+1 to ensure end of interval)

        # Sort events, with ties resolved by placing starts before ends
        events.sort()
        
        max_active = 0
        current_active = 0

        # Process each event
        for _, event in events:
            current_active += event
            max_active = max(max_active, current_active)
        
        return max_active