#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0 ## 慢指针
        for i in range(len(nums)): ##快指针遍历数组
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
        return nums

                

# @lc code=end

