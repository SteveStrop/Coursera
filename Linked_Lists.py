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
        element = self.head
        count = 0
        display_string = ""
        while True:
            display_string += f"Node {count}: {element.data,element.node}\n"
            count += 1
            element = element.node
            if element is None:
                break

        return display_string

    def pop(self):
        if self.is_empty():
            # self.head = Node(None)  # need this because self.head can be set to None if stack becomes empty
            return None
        data = self.head.data
        self.head = self.head.node
        self.n -= 1
        return data

    def is_empty(self):
        return self.n == 0


class Queue:

    def __init__(self):
        # self.first = Node(None)
        self.last = Node(None)
        self.first = Node(None)  # need to initialise all instance variables in the constructor (?)
        self.n = 0

    def enqueue(self, data):
        new_node = Node(data)  # create new last node for the new data
        self.last.node = new_node  # set the current self.last node pointer to the new node (previously this was None)
        self.last = new_node  # rename the current self.last to point to the newly created (and now last) node (whose
        #  .node property  is None)
        if self.is_empty():
            self.first = self.last
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.first.data
        self.first = self.first.node
        self.n -= 1
        return data

    def is_empty(self):
        return self.n == 0

    def __sizeof__(self):
        return self.n

    def __repr__(self):
        item = self.first
        count = 0
        display_string = ""
        while True:
            display_string += f"Node {count}: {item.data,item.node}\n"
            count += 1
            item = item.node
            if item is None:
                break

        return display_string

    # def __enqueue__(self, data):  # not used superseded by enqueue below
    #     body = self.last
    #     self.last = Node(data)  # this is a new node
    #
    #     if self.is_empty():
    #         self.first = self.last
    #     else:
    #         body.node = self.last  # this adds body.node to self.first.node recursively ???? How is body node and
    #         # self.first.node linked?
    #     self.n += 1


def test_stack():
    print("-" * 100 + "Stack" + "-" * 100)
    s = Stack()
    print(f"Newly instantiated Stack: {s}")
    stack_size = 5
    for i in range(stack_size):
        s.push(i)
    print(f"{stack_size} item stack:\n{s}")
    print(f"Pop all {stack_size} elements")
    while not s.is_empty():
        print(s.pop())
    print("\nPopping from an empty stack:")
    print(s.pop())
    print(s.pop())
    print(f"Adding to the existing stack:")
    s.push("new")
    s.push("data")
    print(s)
    print("\nPopping from the stack:")
    while not s.is_empty():
        print(s.pop())


def test_queue():
    print("-" * 100 + "Queue" + "-" * 100)
    q = Queue()
    print(f"Newly instantiated queue is {q}")
    queue_size = 5
    for i in range(queue_size):
        q.enqueue(i)
    print(f"{queue_size} item queue:\n{q}")
    print(f"Dequeue all {queue_size} elements")
    while not q.is_empty():
        print(q.dequeue())
    print("\nDequeue-ing from an empty stack:")
    print(q.dequeue())
    print(q.dequeue())

    print(f"Adding to the existing queue:")
    q.enqueue("new")
    q.enqueue("data")
    print(q)
    print("\nDequeue-ing from the queue:")
    while not q.is_empty():
        print(q.dequeue())


test_stack()

test_queue()
