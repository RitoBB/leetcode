#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        flag = 0
        down = 0
        ## 从后向前遍历,找第一组升序。
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                flag = 1
                down = i-1
                break
        ## flag==0, 不存在下一个更大排列的情况。
        if flag ==0:
            return nums.sort()
        ## 从后向前遍历，找到靠右的第一个比down大的数字。
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[down]:
                nums[i],nums[down] = nums[down],nums[i]
                last = nums[down+1:]
                last.sort()
                nums[down+1:] = last
                return nums
        
# @lc code=end

