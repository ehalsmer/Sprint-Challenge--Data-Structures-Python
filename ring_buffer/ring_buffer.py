from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        # Check if size is equal to capacity
        if self.size < self.capacity:
            self.storage.add_to_tail(item)
            # point new tail at head
            self.storage.tail.next = self.storage.head
        else:
            # remove head, add to tail, point new tail at new head (head has been overwritten by new tail)
            self.storage.remove_from_head
            self.storage.add_to_tail(item)
            self.storage.tail.next = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
