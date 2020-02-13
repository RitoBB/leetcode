#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        candidates.sort()
        def backtrack(path,summ,index):
            if summ == target and path not in res:
                res.append(path)
                return 
            elif summ >target:
                return
            elif summ <target:
                for i in range(index, len(candidates)):
                    backtrack(path+[candidates[i]], summ+candidates[i],i+1)
        backtrack([],0,0)
        return res



# @lc code=end

