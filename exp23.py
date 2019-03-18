# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if pHead == None:
            return None
        is_cycle, pNode = self.have_cycle(pHead)
        p1 = p2 = pHead
        if is_cycle:
            cur = pNode.next
            count = 0
            while (cur != pNode):
                cur = cur.next
                count += 1
            print(count)
            while (count != 0):
                p2 = p2.next
                count -= 1
            print count
            while (p2 != p1):
                p2 = p2.next
                p1 = p1.next
            return p1
        return None

    def have_cycle(self, pHead):
        p1 = p2 = pHead
        while (p2.next):
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True, p1
        return False, p1


def generate_node(arr):
    if arr < 1:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    cur.next = head
    return head

def print_node(head):
    p = head
    while p:
        print "print_node",p.val
        p = p.next

def main():
    a = Solution()
    list_node = generate_node([1,2,3,4,5])
    res = a.EntryNodeOfLoop(list_node)
    res


if __name__ == '__main__':
    main()