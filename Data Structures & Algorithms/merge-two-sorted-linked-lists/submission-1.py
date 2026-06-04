# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        dummy = ListNode()
        tail = dummy

        while l1 and l2: # You can check both lists in one loop
            if l1.val <= l2.val: # Compare the lists against each other
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next 
        tail.next = l1 if l1 else l2 # Gets the final missing node
        return dummy.next
