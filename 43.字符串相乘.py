#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_len, num2_len = len(num1), len(num2)

        res = ['0']*(num1_len+num2_len)

        for i in range(num2_len-1, -1, -1):
            for j in range(num1_len-1,-1,-1):
                tmp = int(num1[j]) * int(num2[i]) + int(res[i+j+1])
                res[i+j+1] = str(tmp%10)
                res[i+j] = str(int(res[i+j])+tmp//10)

        ## 找出第一个不为0的，把后面的合并起来
        for i in range(num1_len+num2_len):
            if res[i] != '0': ##注意：这里的0是str
                return ''.join(res[i:])
        return '0'
        


# @lc code=end

