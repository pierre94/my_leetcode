# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_21
@time: 2018/7/8 下午7:06
"""


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = ListNode2List(l1)
        l2_list = ListNode2List(l2)
        l_list = l1_list + l2_list
        l_list.sort()
        return (l_list)
        # return List2ListNode(l_list) # 标准答案不需要是ListNode 有点奇怪


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def ListNode2List(l):
    l_no = 0  # 10 ** l_no
    l_list = []
    while l:
        l_list.append(l.val)
        l_no = l_no + 1
        l = l.next
    return l_list


def List2ListNode(l_list):
    print l_list
    node_list = []
    for i in range(0, len(l_list)):
        # print "i:", i  # debug
        node_list.append(ListNode(int(l_list[i])))
    for i in range(0, len(node_list) - 1):
        node_list[i].next = node_list[i + 1]
    return node_list[0]


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

print ListNode2List(List2ListNode(ListNode2List(l2)))
# print List2ListNode(l1)


solution = Solution()
print (solution.mergeTwoLists(l1, l2)).val
