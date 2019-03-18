# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead2:
            return pHead1
        if not pHead1:
            return pHead2
        if pHead1.val > pHead2.val:
            p_merged = pHead2
            p_merged.next = self.Merge(pHead1, pHead2.next)
        else:
            p_merged = pHead1
            p_merged.next = self.Merge(pHead1.next, pHead2)
        return p_merged

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
    list_node = generate_node([1,2,4])
    list_node2 = generate_node([3,5])
    res = a.Merge(list_node, list_node2)
    print_node(res)


if __name__ == '__main__':
    main()