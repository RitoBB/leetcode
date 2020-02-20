#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution:
    ## 错误版本
    def subarraySum(self, nums: List[int], k: int) -> int:        
        d = {0:1} ## key: 元素, value: 次数
        count = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if (s-k) in d:
                count += d[s-k]
            d[s] = d.get(s,0)+1 
        return count  
            

        
# @lc code=end

