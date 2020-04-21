# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_head = ListNode(0)
        i, j = l1, l2
        carry = 0
        current = node_head
        
        while i or j or carry:
            if not i and not j and carry:
                current.next = ListNode(carry)
                break
            
            sum_of_ints = (i.val if i else 0) + (j.val if j else 0) + carry
            carry = int(sum_of_ints / 10)
            sum_of_ints %= 10
            
            current.next = ListNode(sum_of_ints)
            
            current = current.next
            i = i.next if i else None
            j = j.next if j else None
        
        return node_head.next
