# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def __init__(self):
        self.new_copy = None
    # 返回 RandomListNode
    def Clone(self, pHead):
        self.clone_head(pHead)
        self.connect_random(pHead)
        return self.reconstruction(pHead)

    def clone_head(self, pHead):
        cur = pHead
        while(cur):
            new_clone = RandomListNode(cur.label)
            new_clone.next = cur.next
            new_clone.random = None

            cur.next = new_clone
            cur = new_clone.next

    def connect_random(self, pHead):
        cur = pHead
        while(cur):
            new_cloned = cur.next
            if cur.random:
                new_cloned.random = cur.random.next
            cur = new_cloned.next

    def reconstruction(self, pHead):
        cur = pHead
        p_clone_head = None
        p_clone_node = None
        if cur != None:
            p_clone_head = p_clone_node = cur.next
            cur.next = p_clone_node.next
            cur = cur.next

        while(cur):
            p_clone_node.next = cur.next
            p_clone_node = p_clone_node.next
            cur.next = p_clone_node.next
            cur = cur.next

        return p_clone_head