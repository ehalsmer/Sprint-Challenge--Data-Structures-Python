from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0
        self.incr = 0

    def append(self, item):
        # Check if size is equal to capacity
        print('self.size', self.size)
        if self.size < self.capacity:
            self.storage.add_to_tail(item)
            # point new tail at head
            self.storage.tail.next = self.storage.head
            self.size += 1
            self.current = self.storage.head
        else:
            # remove head, add to tail, point new tail at new head (head has been overwritten by new tail)
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            self.storage.tail.next = self.storage.head
            self.storage.head.prev = self.storage.tail
            self.incr += 1
            # self.current = self.current.prev

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        j = 0
        if self.incr != 0:
            while j < self.incr:
                current = current.prev
                j += 1
        i = 0
        print(current.value)
        while i < self.size:
            i += 1
            list_buffer_contents.append(current.value)
            current = current.next
        #  returns all of the elements in the buffer in a list in their given order.

        return list_buffer_contents


# myrb = RingBuffer(5)
# myrb.append('a')
# myrb.append('b')
# myrb.append('c')
# myrb.append('d')
# myrb.append('e')
# myrb.append('f')
# print(myrb.get())
# myrb.append('g')
# print(myrb.get())
# print(myrb.storage.tail.value, myrb.storage.tail.next.value)







# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
