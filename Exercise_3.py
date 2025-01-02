class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None
        
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current:
            if current.data == key:
                prev.next = current.next
                return
            else:
                prev = current
                current = current.next
        print(f"{key} is not present in the list.")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    current = sll.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    
    print("Finding 2:")
    found = sll.find(2)
    print(found.data if found else "Not Found")

    print("Removing 2:")
    sll.remove(2)
    current = sll.head
    while current:
        print(current.data, end= " -> ")
        current = current.next
    print("None")