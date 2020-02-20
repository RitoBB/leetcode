#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums)//2
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
            if d[i] > target: ##注意这里不能是大于等于。
                return i
                
        
# @lc code=end

