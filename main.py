# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def print(self):
        print("Printing Linked List: ")
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        for i in range(position-1):
            if current.next == None:
                return None
            current = current.next
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        for i in range(position-2):
            current = current.next
        temp = current.next
        current.next = new_element
        current.next.next = temp

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
            return
        while(current.next.value != value):
            current = current.next
        current.next = current.next.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.print()
    ll.append(e2)
    ll.print()
    ll.append(e3)
    ll.print()


    # Test get_position
    print("Should print 3")
    print(ll.head.next.next.value)
    # Should also print 3
    print("Should print 3")
    print(ll.get_position(3).value)

    # Test insert
    ll.insert(e4,3)
    # Should print 4 now
    print("Should print 4 after insert")
    print(ll.get_position(3).value)
    print(ll.print())

    # Test delete
    ll.delete(1)
    # Should print 2 now
    print("Should print 2 after delete")
    print(ll.get_position(1).value)
    print("Should print 4")
    # Should print 4 now
    print(ll.get_position(2).value)
    print("Should print 3")
    # Should print 3 now
    print(ll.get_position(3).value)