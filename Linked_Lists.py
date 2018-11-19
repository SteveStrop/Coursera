class Node:

    def __init__(self, data):
        self.data = data
        self.node = None


class Stack:

    def __init__(self):
        self.head = Node(None)
        self.n = 0

    def __sizeof__(self):
        return self.n

    def push(self, data):
        new_node = Node(data)
        new_node.node = self.head
        self.head = new_node
        self.n += 1

    def __repr__(self):
        item = self.head
        count = 0
        result = ""
        while item.data is not None:
            result += f"Node {count}: {item.data,item.node}\n"
            count += 1
            item = item.node
        return result

    def pop(self):
        result = self.head.data
        self.head = self.head.node
        self.n -= 1
        return result

    def is_empty(self):
        return self.n == 0


class Queue:

    def __init__(self):
        self.first = Node(None)
        self.last = Node(None)
        self.n = 0

    def __sizeof__(self):
        return self.n

    def enqueue2(self, data):
        body = self.last
        self.last = Node(data)  # this is a new node

        if self.is_empty():
            self.first = self.last
        else:
            body.node = self.last  # this adds body.node to self.first.node recursively ???? How is body node and
            # self.first.node linked?
        self.n += 1

    def enqueue(self, data):
        new_node = Node(data)
        self.last.node = new_node
        self.last = new_node
        if self.is_empty():
            self.first = self.last
        self.n += 1

    def __repr__(self):
        item = self.first
        count = 0
        result = ""
        while True:
            result += f"Node {count}: {item.data,item.node}\n"
            count += 1
            if item.node is None:
                break
            item = item.node
        return result

    def dequeue(self):
        result = self.first.data
        self.first = self.first.node
        self.n -= 1
        return result

    def is_empty(self):
        return self.n == 0


def test_stack():
    print("-" * 100 + "Stack" + "-" * 100)
    s = Stack()
    for i in range(10):
        s.push(i)
    print(s)
    while not s.is_empty():
        print(s.pop())


def test_queue():
    print("-" * 100 + "Queue" + "-" * 100)
    q = Queue()
    for i in range(5):
        q.enqueue(i)
    print(q)
    while not q.is_empty():
        print(q.dequeue())


test_stack()

test_queue()
