#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i,adjacency,flag):
            ## 代表其他节点已经访问过的，无需重复遍历，说明无环，直接返回true
            if flag[i] == -1:
                return True
            ## 代表当前节点启动的dfs，说明本节点已经第2次访问，说明有环，直接返回false
            if flag[i] == 1:
                return False
            ## 当前节点访问，设置为 1
            flag[i] = 1
            ## 递归遍历相邻节点
            for j in adjacency[i]:
                if not dfs(j,adjacency,flag):
                    return False
            ## 遍历完成说明没有环，设为-1
            flag[i] = -1
            return True

        ## 初始化adjacency
        adjacency = [[] for _ in range(numCourses)]
        flag = [0 for _ in range(numCourses)]

        ## 设置adjacency的遍历顺序
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        
        for i in range(numCourses):
            if not dfs(i,adjacency,flag):
                return False
        return True


        
# @lc code=end

