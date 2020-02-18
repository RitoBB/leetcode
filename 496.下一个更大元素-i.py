#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            stack.append(i)
            for j in range(idx+1, len(nums2)):
                while stack and nums2[j] > nums1[stack[-1]]:
                    res[stack.pop()] = nums2[j]
        return res
# @lc code=end

