'''
912
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
'''

'''
手撸快排
'''


class Solution:
    def qsort(self, nums,l,r):
        if l >= r:
            return
        if r-l == 1:
            if nums[r] < nums[l]:
                nums[r],nums[l] = nums[l],nums[r]
            return 

        il,ir = l,r
        mid = randint(l,r) # 艹，居然卡我mid的数据
        # print(l,r)
        flag = nums[mid]
        while il<ir:
            while il < mid and nums[il]<=flag:
                il += 1
            nums[mid],nums[il] = nums[il],flag
            mid = il
            # print(nums)

            while ir > mid and nums[ir]>=flag:
                ir -= 1
            nums[mid],nums[ir] = nums[ir],flag
            mid = ir

            # print(nums)

        self.qsort(nums,l,mid-1)
        self.qsort(nums,mid+1,r)            
        

    def sortArray(self, nums: List[int]) -> List[int]:
        Solution().qsort(nums,0,len(nums)-1)
        return nums