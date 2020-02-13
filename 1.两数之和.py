#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i,v in enumerate(nums):
            hashmap[v] = i
        for i, num in enumerate(nums):
            j = hashmap.get(target-num)
            if i != j and j!= None:
                return [i,j]


# @lc code=end

