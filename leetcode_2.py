# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: leetcode_2
@time: 2018/6/30 下午1:02

给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return Num2ListNode(ListNode2Num(l1) + ListNode2Num(l2))


def ListNode2Num(l):
    l_num = 0
    l_no = 0  # 10 ** l_no
    while l:
        l_num = l_num + 10 ** l_no * l.val
        l_no = l_no + 1
        l = l.next
    return l_num


def Num2ListNode(num):
    num_list_ = (list(str(num)))
    num_list = num_list_[::-1]
    node_list = []
    for i in range(0, len(num_list)):
        # print "i:", i  # debug
        node_list.append(ListNode(int(num_list[i])))
    for i in range(0, len(node_list) - 1):
        node_list[i].next = node_list[i + 1]
    return node_list[0]


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# print ListNode2Num(Num2ListNode(ListNode2Num(l1)))
# print ListNode2Num(l1)
# print ListNode2Num(l2)
solution = Solution()
print ListNode2Num(solution.addTwoNumbers(l1, l2))
