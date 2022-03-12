# Task constraints
"""
无太多限制，需要考虑空间限制
"""
# Idea generation
'''
链表的特性：内存分配可以不连续; 每个节点用两个基础数据类型就可以表示，
    一个是节点的值, 另一个存储下一节点的地址, 最末端的节点指向nil; 
    从某个节点开始只能找到这个节点之后的节点

反转：即反过来指向, 即需要知道两个节点的地址
需要遍历，是否需要另外开辟空间，可能有两种方法：
    1. 不修改原有的链表，需要另外开辟空间，倒叙遍历即可；(递归)
    2. 直接修改原有的链表，不需要另外开启空间（迭代）

'''
# Complexity
"""
时间复杂度和空间复杂度应该都为log(n)
"""
# Writing the code

class ListNode(object):
    def __init__(self, x) -> None:
        self.val = x
        self.next = None
        pass

class Solution(object):
    def reverseList(self, head) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while(curr != None): # 利用中间变量，同比大小转换
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
# 
"""
总结：
链表重新了解，没有理解错，就是代表一个节点
迭代与递归有什么区别？空间的问题？
太不仔细了，画图会直观一些。
即使是一个小项目，也包含了太多的基础的东西，还有可以研究的东西(用引用的方法，可能好理解一点； 变量名与实体对象)
"""
# Testing your code

