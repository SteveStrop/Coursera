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

    def peek(self):
        return self.head.data

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








