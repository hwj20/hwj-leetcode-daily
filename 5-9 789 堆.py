'''
786. K-th Smallest Prime Fraction
Medium
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
'''

'''
我也不懂，想法是一边除一边用堆保存最小的k个，原来python里的堆是一个元素一个元素地比较
'''


class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        min_heap = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                num = float(arr[i])/arr[j]
            # 如果堆的大小小于k，直接添加
                if len(min_heap) < k:
                    heapq.heappush(min_heap, (-num,(arr[i],arr[j])))  # 使用负数转换为最大堆
                else:
                    # 如果新数字小于堆中的最大数字（堆顶），则替换
                    if -min_heap[0][0] > num:
                        heapq.heapreplace(min_heap, (-num,[arr[i],arr[j]]))
        # print(min_heap)
        # 将堆中的数字转换回正数，并返回
        return min_heap[0][1]