#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    ## 二分法： mid和nums[mid]对比
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0 ,len(nums) ##注意这里right不是len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]>mid:
                right = mid
            else:
                left = mid + 1
        return left
    
    ## 求和法
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for idx,num in enumerate(nums):
            res += idx-num
        return res

    ## 位运算法
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for idx,num in enumerate(nums):
            res = res^idx^num
        return res^len(nums)

    
    
# @lc code=end
