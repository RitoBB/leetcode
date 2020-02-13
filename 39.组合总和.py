#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        res = []
        ## 回溯算法
        def backtrack(path,summ,index):
            if summ == target:  ## if 满足结束条件， return
                res.append(path)
            elif summ > target: ## if 不满足， return空
                return 
            elif summ < target:
                for i in range(index,len(candidates)): ## 选择路径
                    backtrack(path+[candidates[i]] , summ+candidates[i],i)
        backtrack([],0,0)
        return res

# @lc code=end

