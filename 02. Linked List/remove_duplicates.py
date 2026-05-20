class ListNode:
    def __init__(self, val=0, next: ListNode = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode = None) -> ListNode:
        if not head:
            return None

        currentNode = head

        while(currentNode and currentNode.next):
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return head

    def printList(self, head: ListNode):
        temp = head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()
            
def main():

    node3 = ListNode(2)
    node2 = ListNode(1, node3)
    head = ListNode(1, node2)

    s = Solution()

    s.printList(head)

    head = s.deleteDuplicates(head)

    s.printList(head)

main()
