#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        m = 0
        while left < right:
            if height[left] < height[right]:
                m = max(m, height[left]*(right-left))
                left += 1
            else:
                m = max(m,height[right]*(right-left))
                right -= 1
        return m

        
# @lc code=end

