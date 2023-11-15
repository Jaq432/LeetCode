class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # create a "dummy" node to serve as the head of the merged list
        dummy = ListNode()
        current = dummy

        # go over both lists
        while list1 is not None and list2 is not None:
            # get the next lowest value
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # move on to the next node
            current = current.next

        # if there's a remaining value, add it to the linked node list
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        # Return the head of the merged list without the first "dummy" node
        return dummy.next
        
