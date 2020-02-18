#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## 方法一： 快速排序 (有点慢)
        def quickSort(left,right):
            key = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < key and nums[r] > key:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= key:
                    l += 1
                if nums[r] <= key:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r
        left, right = 0, len(nums)-1
        while 1:
            idx = quickSort(left, right)
            if idx == k-1:
                return nums[idx]
            elif idx < k-1:
                left = idx + 1 
            elif idx > k-1 :
                right = idx - 1

        ## 方法三： 手动堆
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def adjust_heap(idx, max_len):
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_loc = idx
            if left < max_len and nums[max_loc] < nums[left]:
                max_loc = left
            if right < max_len and nums[max_loc] < nums[right]:
                max_loc = right
            if max_loc != idx:
                nums[idx], nums[max_loc] = nums[max_loc], nums[idx]
                adjust_heap(max_loc, max_len)
        
        # 建堆
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            adjust_heap(i, n)
        res = None
        for i in range(1, k + 1):
            res = nums[0]
            nums[0], nums[-i] = nums[-i], nums[0]
            adjust_heap(0, n - i)
        return res

    def findKthLargest(self, nums: List[int], k: int) -> int:
        ##方法二： 用内置函数heapq
        return heapq.nlargest(k,nums)[-1]
        
# @lc code=end

