#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)
        n = len(nums)
        for i in range(2*n):
            idx = i % n
            while stack and nums[idx]> nums[stack[-1]]:
                res[stack.pop()] = nums[idx]
            stack.append(idx)
        return res

        
# @lc code=end

