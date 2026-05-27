class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Linear Time - O(n )
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string =  f"[{last.value}]"
            while last.next:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"
            return  return_string

    # Linear Time - O(n )
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return  True
            last = last.next
        return False


    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter


    # O(n) - Linear Time
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            # self.size = 1
        else:
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node

            # last = self.head
            # while last.next:
            #     last = last.next
            # last.next = Node(value)
            # self.size += 1

    # O(1) - constant time
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    # O(n) - Linear Time
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise  ValueError("Index out of range")
            else:
                last = self.head
                for i in range(index-1):
                    if last.next is None:
                        raise  ValueError("Index out of range")
                    last = last.next

                new_node = Node(value)
                new_node.next = last.next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node
                last.next = new_node

    # O(n) - Linear Time
    def delete(self, value):
        last = self.head
        if last is not value:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not  None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next


    # O(n) - Linear Time
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head

            for i in range(index-1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            if last.next == None:
                raise ValueError("Index out of bounds")
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                last.next = last.next.next

    # O(n) - Linear Time
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
                return last.value

if __name__ == "__main__":
    ll = DoublyLinkedList()
    # 100, 10,40,650
    ll.append(10)
    ll.insert(50, 1)
    ll.insert(40, 1)
    ll.insert(650, 1)
    ll.insert(556, 1)
    ll.insert(505, 1)
    ll.insert(5089, 1)


    ll.prepend(100)
    ll.insert(20, 1)
    ll.delete(5089)
    ll.delete(50)
    ll.delete(505)
    ll.delete(556)
    ll.pop(1)

    print(ll)