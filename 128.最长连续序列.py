#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    ## 方法一： 并查集合
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for x in nums:
            ## 找出开头
            if x-1 not in nums:
                y = x+1
                while y in nums:
                    y += 1
                res = max(res, y-x)
        return res
        
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

