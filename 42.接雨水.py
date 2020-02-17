#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        ## 方法三： 动态规划：
        # step 1: 初始化left_max, right_max
        if not height:
            return 0
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n
        left_max[0] = height[0]
        right_max[-1] = height[-1]

        # Step 2: 定义转移状态方程
        for i in range(1,n):
            left_max[i] = max(height[i], left_max[i-1])
        for i in range(n-2,-1,-1):
            right_max[i] = max(height[i], right_max[i+1])
        # Step 3: 计算接雨水量
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i])-height[i]
        return res


        ## 方法一： 栈
        if not height:
            return 0
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]]<height[i]:    
                tmp = stack.pop()
                ## 边界情况
                if not stack:
                    break
                res += (min(height[stack[-1]], height[i])-height[tmp]) * (i-stack[-1]-1)
            stack.append(i)
        return res

        ## 方法二： 双指针法
        if not height: 
            return 0
        left, right = 0, len(height)-1
        res = 0
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if right_max > height[right]:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return res

        ##方法三： 动态规划






# @lc code=end

