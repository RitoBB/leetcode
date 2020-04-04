#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        nums.sort()
        res = []
        ## 固定一个指针：i
        for i in range(l-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            ## 当 四个数加起来>target,则直接跳出循环，因为后面不可能还有res
            if nums[i] + sum(nums[i+1:i+3+1]) > target:
                break
             # 如果固定数与数组三最大数之和小于taget, 则当前遍历不存在解, 进入下一个遍历
            if nums[i]+ sum(nums[-1:-3-1:-1]) < target:
                continue
            ##固定第二个指针 ：j
            for j in range(i+1,l-2):
                ## 去重，减枝。j-i >1说明 j与i不重复。
                if j-i >1 and nums[j] == nums[j-1]:
                    continue
                if nums[i]+nums[j] +sum(nums[j+1:j+1+2]) > target:
                    break
                if nums[i] + nums[j] + sum(nums[-1:-2 - 1:-1]) < target:
                    continue
                ##双指针
                left, right = j+1, l-1
                while left < right:
                    tmp_sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if tmp_sum < target:
                        left += 1
                    elif tmp_sum > target:
                        right -= 1
                    else:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
                    ##判断是否重复
                    #求得正确解后，去重（剪枝）
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        return res
                    
                
                # @lc code=end

