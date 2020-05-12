#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        
        def backTrack(count, idx, target, tmp):
            if count == k:
                if target == 0:
                    res.append(tmp)
                return ##注意return应该写在if count == k下，而不是target == 0下
            for i in range(idx,10):
                if i > target:
                    break
                backTrack(count+1, i+1, target - i, tmp+[i])
        backTrack(0,1,n,[])
        return res


# @lc code=end

