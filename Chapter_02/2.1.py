# Remove duplicates from an unsorted linked list

class Node():
    """A single Node in a linked list"""
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        

class LinkedList():
    """A doubly Linked List"""
    def __init__(self, initial_list=[]):
        self.head = None
        self.tail = None
        self.length = 0
        for val in initial_list:
            self.insert(val)

    def insert(self, val):
        """Insert into the back of the list"""
        if self.tail is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            last = self.tail
            self.tail = Node(val)
            last.next = self.tail
            self.tail.prev = last

        self.length += 1

    def insert_front(self, val):
        """Insert into the front of the list"""
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            first = self.head
            self.head = Node(val)
            first.prev = self.head
            self.head.next = first

        self.length += 1

    def delete_back(self):
        """Delete the last item in the list"""
        if self.head == self.tail:
            # This is the only item in the list
            self.head = None
            self.tail = None

        elif self.tail is not None:
            last = self.tail.prev
            # We can assume that last is not None because we 
            # checked for head == tail previously
            last.next = None
            self.tail = last

        if self.length > 0:
            self.length -= 1


    def delete_front(self):
        """Delete the first item in the list"""
        if self.head == self.tail:
            # This is the only item in the list
            self.head = None
            self.tail = None

        elif self.tail is not None:
            first = self.head.next
            # We can assume that first is not None because we 
            # checked for head == tail previously
            first.prev = None
            self.head = first

        if self.length > 0:
            self.length -= 1

    def delete_node(self, node):
        """Delete the specified node"""
        prv = node.prev
        nxt = node.next

        if prv is not None:
            prv.next = nxt
        else:
            self.head = node
        if nxt is not None:
            nxt.prev = prv
        else:
            self.tail = node

        if self.length > 0:
            self.length -= 1

    def traverse_until(self, val, direction="forward"):
        """
        Traverse until we find the first instance of the specified value.
        Then, return the node containing that value. Otherwise, return None.
        """
        if direction == "forward":
            ptr = self.head
        else:
            ptr = self.tail
        while ptr is not None:
            if ptr.val == val:
                return ptr
            if direction == "forward":
                ptr = ptr.next
            else:
                ptr = ptr.prev
        return None

    def __repr__(self):
        """Print the list"""
        ptr = self.head
        ret = []
        while ptr is not None:
            ret.append(ptr.val)
            ptr = ptr.next
        return ''.join(ret)

    def __len__(self):
        return self.length

def remove_duplicates(ll):
    ptr = ll.head
    vals = {}
    while ptr is not None:
        if vals.get(ptr.val):
            # This is a duplicate
            prv = ptr.prev
            nxt = ptr.next

            if prv is not None:
                prv.next = nxt
            if nxt is not None:
                nxt.prev = prv

        vals[ptr.val] = True
        ptr = ptr.next

    return ll

duped = 'abcdbccasdf'
print("before:")
print(duped)
deduped = remove_duplicates(LinkedList(list(duped)))
print("after:")
print(deduped)
