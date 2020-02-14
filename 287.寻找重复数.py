#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ##方法一：
        ## return int((sum(nums) - sum(set(nums)))/ (len(nums) - len(set(nums))))
        ## 方法三： 双指针法
        slow, fast = 0, 0
        while(1):
            slow = nums[slow]
            fast = nums[nums[fast]]
            # print slow, fast
            if slow == fast: # loop exists
                fast = 0
                while(nums[slow] != nums[fast]):
                    slow = nums[slow]
                    fast = nums[fast]
                    # print slow, fast
                return nums[fast]
        """
        ##方法二：二分法
        left, right = 1, len(nums) - 1
        while(left < right):
            mid = left + (right - left) //2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            # print mid, count
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left
        """

# @lc code=end

