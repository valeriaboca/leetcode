
# 206. Reverse Linked List
# def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
#        prev, curr = None, head
#        while curr:
#            nextPointer = curr.next
#            curr.next = prev
#            prev = curr
#            curr = nextPointer
#        return prev