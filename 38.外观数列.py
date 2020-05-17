#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        ## 外循环 + 内循环
        ## 外循环： 给定上个人报的数，求下个人报的数
        ## 内循环： 遍历上个人报的数
        prev = '1' ##记录上一个
        for i in range(1,n):
            next = ''
            num = prev[0]
            count = 1 ## 记录num出现了多少次
            for j in range(1, len(prev)):
                if prev[j] == num:
                    count += 1
                else:
                    next += str(count) + num
                    num = prev[j]
                    count = 1
            next += str(count) + num
            prev = next
        return prev


# @lc code=end

