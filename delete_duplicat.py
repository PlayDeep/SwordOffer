# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        cur = pHead
        res = []
        while cur and cur.next:
            tmp = cur.val
            if cur.val == cur.next.val:
                value = cur.val
                while cur and value == cur.val:
                    cur = cur.next
                continue
            else:
                res.append(cur)
            cur = cur.next
        if cur != None:
            res.append(cur)
        if len(res) > 0:
            for i in range(1, len(res)):
                res[i-1].next = res[i]
                res[i].next = None
        return res[0]


def generate_node(arr):
    if arr < 1:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

def print_node(head):
    p = head
    while p:
        print "print_node",p.val
        p = p.next

def main():
    a = Solution()
    list_node = generate_node([1,2,3,3,4,4,5])
    res = a.deleteDuplication(list_node)
    print_node(res)


if __name__ == '__main__':
    main()