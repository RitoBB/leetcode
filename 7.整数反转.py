#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    ## 方法一： 暴力
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != '-':
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0
        
    ## 方法二： 设置边界
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        #则其数值范围为 [−2^31,  2^31 − 1]
        boundary = (1<<31) -1 if x>0 else 1<<31

        while y!= 0:
            res = res*10 + y%10
            if res > boundary:
                return 0
            y //= 10
        return res if x>0 else -res

    
# @lc code=end

