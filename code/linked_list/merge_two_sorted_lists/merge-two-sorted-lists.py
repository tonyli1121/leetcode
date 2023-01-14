# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None :
            return list2
        elif list2 == None:
            return list1
        
        head1 = list1
        head2 = list2
        
        prev = None # Most important pointer it will make all the links
        
        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                if prev != None:
                    prev.next = head1
                prev = head1
                head1 = head1.next         
            else:
                if prev != None:
                    prev.next = head2
                prev = head2
                head2 = head2.next
                
        if head1 != None:
            prev.next = head1
        else:
            prev.next = head2
        
        if list1.val <= list2.val:
            return list1
        else:
            return list2
