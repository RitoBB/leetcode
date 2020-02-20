#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
from functools import cmp_to_key
class Solution:
    ## 方法一
    def largestNumber(self, nums: List[int]) -> str:
        def helper(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        return "".join(sorted(map(str, nums), key=cmp_to_key(helper))).lstrip("0") or "0"


    

    

# @lc code=end

