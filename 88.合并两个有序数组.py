#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## 双指针
        end = m+n-1
        end1 = m-1
        end2 = n-1
        while end1 >=0 and end2 >=0 :
            if nums1[end1] >= nums2[end2]:
                nums1[end] = nums1[end1]
                end -= 1
                end1 -= 1
            else:
                nums1[end] = nums2[end2]
                end2 -= 1
                end -= 1
        nums1[:end2+1] = nums2[:end2+1]



# @lc code=end

