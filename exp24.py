# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        res = []
        while(pHead != None):
            res.append(pHead)
            pHead = pHead.next
        rHead = res[-1]
        cur = rHead
        for i in range(len(res)-1, 0,-1):
            cur.next = res[i]
            cur = cur.next
        return rHead