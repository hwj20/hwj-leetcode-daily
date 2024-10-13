'''
632
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
'''


'''

'''

from heapq import heappush, heappop
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        
        # Initialize the heap and find the initial max
        for i in range(len(nums)):
            heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
        
        # Initialize range with very large bounds
        best_range = [float('-inf'), float('inf')]
        
        # Process the heap
        while min_heap:
            min_val, row, idx = heappop(min_heap)
            
            # Update the best range
            if current_max - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, current_max]
            
            # Move to the next element in the current row
            if idx + 1 < len(nums[row]):
                next_val = nums[row][idx + 1]
                heappush(min_heap, (next_val, row, idx + 1))
                current_max = max(current_max, next_val)
            else:
                # If any list is exhausted, the range can no longer cover all lists
                break
        
        return best_range
