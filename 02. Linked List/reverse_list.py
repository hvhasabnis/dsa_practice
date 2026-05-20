class ListNode:
    def __init__(self, val=0, next: ListNode = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode = None) -> ListNode:
        if not head:
            return None
        
        currentNode = head

        prev = None

        next = None

        while(currentNode):
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next

        return prev
    
    def printList(self, head: ListNode):
        temp = head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
def main():

    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    s = Solution()
    
    s.printList(head)
    
    head = s.reverseList(head)

    s.printList(head)

main()