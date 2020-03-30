#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        appro= float(inf)
        for k in range(len(nums)-2):
            i ,j = k+1, len(nums)-1
            while i < j:
                s = nums[k] +nums[i] + nums[j]
                if s == target:
                    return s
                elif s< target:
                    i += 1
                elif s > target:
                    j -= 1
                if abs(s-target) < appro:
                    appro = abs(s-target)
                    res = s
        return res

    
# @lc code=end

