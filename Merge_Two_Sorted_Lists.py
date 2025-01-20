#21. Merge Two Sorted Lists
#You are given the heads of two sorted linked lists list1 and list2. 
#Write a function mergeTwoLists that merges the two lists into a single sorted linked list.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node that will serve as the start of the merged list.
        # This helps in simplifying edge cases like when both lists are empty.
        dummy = ListNode()
        
        # Set the 'current' pointer to the dummy node. This will be used to
        # build the new merged list by updating current.next.
        current = dummy
        
        # Iterate through both lists as long as both lists are not empty.
        while list1 and list2:
            # Compare the values of the current nodes in both lists.
            if list1.val < list2.val:
                # If list1's current node has a smaller value, attach it to the merged list.
                current.next = list1
                
                # Move the list1 pointer to the next node.
                list1 = list1.next
            else:
                # Otherwise, list2's current node has a smaller value, attach it to the merged list.
                current.next = list2
                
                # Move the list2 pointer to the next node.
                list2 = list2.next
            
            # Move the 'current' pointer to the last node of the merged list.
            current = current.next
        
        # After one of the lists is exhausted, if list1 still has nodes, append the rest of list1.
        if list1:
            current.next = list1
        
        # If list2 still has nodes, append the rest of list2.
        elif list2:
            current.next = list2
        
        # Return the merged list starting from the node after the dummy node.
        # The dummy node is just a placeholder to help with list manipulation.
        return dummy.next

        # The following lines are unnecessary and not needed for merging linked lists.
        list1.sort()  # Sorting list1 is not required in this approach.
        return list1  # Returning list1 is incorrect because the merged list has already been returned above.
