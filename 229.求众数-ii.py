#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = [] # 返回数组
        majorityO = -1 # 候选人1
        majorityT = -1 # 候选人2
        countO = 0 # 候选人1 票数
        countT = 0 # 候选人2 票数
        
        for num in nums:
            if countO == 0 and num != majorityT:
                majorityO = num
                countO += 1
                continue
            elif countT == 0 and num != majorityO:
                majorityT = num
                countT += 1
                continue
            else:
                if majorityO == num:
                    countO += 1
                elif majorityT == num:
                    countT += 1
                else:
                    countO -= 1
                    countT -= 1
        counterO = 0
        counterT = 0
        ## 计数   
        if countO > 0:
            for num in nums:
                if num == majorityO:
                    counterO += 1
        if counterO > len(nums)//3:
            res.append(majorityO)
        if countT > 0:
            for num in nums:
                if num == majorityT:
                    counterT += 1
        if counterT > len(nums)//3:
            res.append(majorityT)
        
        return res


# @lc code=end

