#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k ==0 or k>len(nums):
            return []
        max_list = []
        start, end = 0, k
        while end <= len(nums):
            max_list.append(max(nums[start:end]))
            start += 1
            end +=1
        return max_list

        
# @lc code=end
