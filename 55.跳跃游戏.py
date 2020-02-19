#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ## 方法二： 从后往前跳
        n = len(nums)
        start, end = n-2, n-1
        while start >= 0:
            end = max(end, start)
            start -= 1
        return end <= 0
    



    def canJump(self, nums: List[int]) -> bool:
        ## 方法一： 从前往后跳
        start, end = 0, 0
        while start <= end and end < len(nums)-1:
            end = max(end, start+nums[start])
            start += 1
        return end >= len(nums)-1



        
# @lc code=end

