# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        linked_list, stack = [], []
        
        while head:
            linked_list.append(head.val)
            head = head.next

        ans = [0] * len(linked_list)

        for i in range(len(linked_list) - 1, -1, -1):
            while stack and stack[-1] <= linked_list[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(linked_list[i]) 
        
        return ans
            
        
                    