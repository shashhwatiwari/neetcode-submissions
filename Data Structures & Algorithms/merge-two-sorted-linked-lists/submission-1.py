# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        standin = ListNode()
        prev = standin
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1 # assign the next to a node of list 1
                list1 = list1.next
            else:
                prev.next = list2 # assign the next to a node of list 2
                list2 = list2.next
            prev = prev.next # actually move to that node that you just assigned to either list 1 or list 2
        
        # if there are any leftovers in either of the lists
        if list1:    
            prev.next = list1 # we do prev.next because last line of while loop increments pointer to the last filled node, therefore, if dont do next we will overwrite one node.
        else:
            prev.next = list2
        return standin.next