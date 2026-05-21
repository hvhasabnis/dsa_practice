class ListNode:
    def __init__(self, val=0, next: ListNode = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode = None, list2: ListNode = None) -> ListNode:
        if not list1:
            if not list2:
                return None
            else:
                return list2
        elif not list2:
            return list1
        
        current1 = list1

        current2 = list2

        head = None

        if current1.val <= current2.val:
            head = current1
            current1 = current1.next
        else:
            head = current2
            current2 = current2.next

        newList = head
        
        while current1 and current2:
            if current1.val <= current2.val:
                newList.next = current1
                current1 = current1.next
            else:
                newList.next = current2
                current2 = current2.next
            
            newList = newList.next

        if current1:
            newList.next = current1
        else:
            newList.next = current2

        return head
    
    def printList(self, head: ListNode):
        temp = head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()

def main():
    node3 = ListNode(4)
    node2 = ListNode(3, node3)
    list1 = ListNode(2, node2)

    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    list2 = ListNode(1, node2)

    s = Solution()

    head = s.mergeTwoLists(list1, list2)

    s.printList(head)


main()