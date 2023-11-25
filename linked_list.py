class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if not self.head:
            self.head = new_element
            return
        while current.next:
            current = current.next
        current.next = new_element
    
    def print(self):
        current = self.head
        if not current:
            print("Empty Linked List!")
            return
        while current:
            print(current.value)
            current = current.next

    def remove(self, value):
        # removes the first occurance of an element from the Linked List
        current = self.head
        if not current:
            print("Cannot remove elements from an empty LinkedList!")
        elif current.value == value:
            self.head = current.next
        elif current.next.value == None:
            print("Could not find the element in the List")
        else:
            while current.next.value != value:
                current = current.next
                if current.next.value == None:
                    print("Could not find the element in the List")
                    return
            current.next = current.next.next
        return

if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    ll = LinkedList()
    ll.append(e1)
    ll.append(e2)
    ll.append(e3)
    ll.append(e4)
    print("Before removing 3")
    ll.print()

    ll.remove(3)

    print("After removing 3")
    ll.print()