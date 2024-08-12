'''
703
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''


'''
考一考你们类的语法
'''
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.idx = k-1
        self.h = [x for x in nums]
        heapq.heapify(self.h)
        while len(self.h)>k:
            heapq.heappop(self.h)
        # print(self.h)
            
        # heapq.heapify(self.h)

    def add(self, val: int) -> int:
        if self.h == []:
            self.h = [val]
            return val
        if val > self.h[0] or len(self.h)<self.idx+1:
            heapq.heappush(self.h,val)
        while len(self.h)>self.idx+1:
            heapq.heappop(self.h)
            # heapq.heappop(self.h)
        # print(self.h)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)