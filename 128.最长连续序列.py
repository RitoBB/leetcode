#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    ## 方法二： 字典
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = {}
        res = 0
        for num in nums:
            if num not in lookup:
                left = lookup[num-1] if num-1 in lookup else 0
                right = lookup[num+1] if num+1 in lookup else 0
                # 记录长度
                lookup[num] = left + right + 1
                ## 把头尾都设置为最长长度
                lookup[num-left] = left + right + 1
                lookup[num+right] = left + right + 1
                res = max(res, left+right+1)
        return res

                
        
# @lc code=end

