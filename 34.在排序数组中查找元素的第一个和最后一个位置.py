#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            n = nums[mid]
            if n == target:
                tmp = mid
                while tmp > 0 and nums[tmp-1] == target:
                    tmp -= 1
                while mid < len(nums) - 1 and nums[mid+1] == target:
                    mid += 1
                return [tmp,mid]              
            elif n < target:l = mid+1
            else:r = mid-1
        return [-1,-1]



# @lc code=end

