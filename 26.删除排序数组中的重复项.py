#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## 方法二：从前往后遍历，指针法
        if len(nums) <= 1:
              return len(nums)
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1
        

    def removeDuplicates(self, nums: List[int]) -> int:
        ## 方法一：从后往前遍历
        for i in range(len(nums)-1,-1,-1):
            if i-1 != -1:
                if nums[i-1] == nums[i]:
                    del nums[i]
        return len(nums)


        




# @lc code=end

