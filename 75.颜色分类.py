#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ## two-pointers
        index = 0
        i,j = 0, len(nums)-1
        while index <= j:
            if nums[index] == 0:
                nums[i],nums[index] = nums[index],nums[i]
                i += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            elif nums[index] == 2:
                nums[j], nums[index] = nums[index], nums[j]
                j -= 1
        return nums
        
        
# @lc code=end

