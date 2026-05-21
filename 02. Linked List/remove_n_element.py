class ListNode:
    def __init__(self, val=0, next: ListNode = None):
        self.val = val
        self.next = next
    
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        
        current = head

        count = 0

        while current:
            count += 1
            current = current.next

        if n > count:
            return head
        
        pos = count - n - 1

        current = head
    
        while pos != 0:
            current = current.next
            pos -= 1

        temp = current.next

        current.next = current.next.next

        temp.next = None

        del temp

        return head
    
    def printList(self, head: ListNode):
        temp = head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
def main():
    node6 = ListNode(6)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    s = Solution()

    head = s.removeNthFromEnd(head, 2)

    s.printList(head)

main()
