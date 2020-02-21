#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        else:
            self.d[val] = len(self.l) ## 现存储，key是val,value是在list中的index
            self.l.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            self.d[self.l[-1]] = self.d[val]  ##替换要删除的哈希表中的值，用其他来代替。
            self.l[self.d.pop(val)] = self.l[-1] #把数组最后一个元素取下来顶替被删除元素位置O(1)
            self.l.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.l[random.randint(0,len(self.l)-1)]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

