#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    ##方法二：
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left

    ##方法一：
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# @lc code=end

