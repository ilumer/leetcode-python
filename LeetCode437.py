# coding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        return self.path(root, sum) + self.pathSum(root.left, sum) + \
            self.pathSum(root.right, sum)
        # 将每个子树都看成一个root　然后代入到目标中

    def path(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        path = 1 if root.val == sum else 0
        return path + self.path(root.left, sum - root.val) + \
            self.path(root.right, sum - root.val)
        # 在某个子树下存在几种可能


# https://leetcode.com/problems/path-sum-iii/discuss/91878/17-ms-O(n)-java-Prefix-sum-method
# 这个方法效率更高　同时也更有意思
# current - target = x 即　current -x = target　可以找到目标的路径
# preSum.put(currSum, preSum.get(currSum) - 1); 是为了避免出现左右节点连接的情况形成可以使用的path
