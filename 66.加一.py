#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    ## 方法二，判断最后一位是否为9，如果不是直接加一，如果是则变为0
    ## 时间复杂度： O(N)
    ## 空间复杂度： O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!= 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0,1)
        return digits

    ## 方法一： 暴力，转化int和str,并map
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str,digits))) + 1
        res = list(map(int,*[str(num)]))
        return res
    
        
# @lc code=end

