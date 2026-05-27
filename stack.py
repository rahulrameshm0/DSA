class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # O(1) - constant time
    def __len__(self):
        return self.size

    def __repr__(self):
        items = []
        current_item = self.top

        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return ', '.join(items)


    # O(1) - Constant Time
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        self.size += 1

    # O(1) - constant time
    def pop(self):
        if self.top is None:
            raise  ValueError("stack is empty")
        pop_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return pop_value

    # O(1) - constant time
    def peek(self):
        if self.top is None:
            raise  ValueError("stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None

if __name__ == '__main__':
    stack = Stack()

    print("PUSH")
    stack.push(10)
    stack.push(5)
    stack.push(20)
    stack.push(15)

    print(stack)

    print("PEAK")

    print(stack.peek())


    print("Stack Empty")
    print(stack.is_empty())

    print("POP")
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)




