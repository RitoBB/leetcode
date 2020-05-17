#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ## 字典
        lookup = defaultdict(list)
        for s in strs:
            lookup[''.join(sorted(s))].append(s)
        return list(lookup.values())
# @lc code=end

