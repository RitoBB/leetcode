#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ## 二分法
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2 ##注意，是在while循环中设置
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left ## 返回left





        
# @lc code=end

