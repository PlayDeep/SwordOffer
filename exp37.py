# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    flag = -1

    def Serialize(self, root):
        s = ''
        s = self.recursion_serialize(root, s)
        return s

    def recursion_serialize(self, root, s):
        if root is None:
            s = '$,'
            return s
        s = str(root.val) + ','
        left = self.recursion_serialize(root.left, s)
        right = self.recursion_serialize(root.right, s)
        s = s + left + right
        return s


    def Deserialize(self, s):
        l = s.split(',')
        self.flag += 1
        if len(s) < self.flag:# 为什么是s不是l呢？
            return None
        root = None
        if l[self.flag] != '$':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root