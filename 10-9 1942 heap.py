'''
1942
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.
'''

'''
heap
'''

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        import heapq
        tar = times[targetFriend]
        # print(tar)
        times.sort(key=lambda x:x[0])
        h = []
        s = []
        cnt = 0
        for t in times:
            while h and t[0] >= h[0][0]:
                heapq.heappush(s,heapq.heappop(h)[1])
            if s:
                seat = heapq.heappop(s)
            else:
                seat = cnt
                cnt += 1
            if t[0] == tar[0]:
                return seat
            heapq.heappush(h,(t[1],seat))
        return -1