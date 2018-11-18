class Node:

    def __init__(self, data):
        self.data = data
        self.link = None


# head = None
# for i in range(10):
#     new_node = Node(i)
#     new_node.link = head
#     head = new_node
#     print_nodes(head)


class Stack:

    def __init__(self):
        self.head = Node(None)
        self.n = 0

    def __sizeof__(self):
        return self.n

    def push(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node
        self.n += 1

    def __str__(self):
        item = self.head
        count = 0
        result = ""
        while item.link is not None:
            result += f"Node {count}: {item.data,item.link}\n"
            count += 1
            item = item.link
        return result

    def pop(self):
        result = self.head.data
        self.head = self.head.link
        self.n -= 1
        return result

    def is_empty(self):
        return self.n == 0


print("-" * 100 + "Stack" + "-" * 100)
s = Stack()

data = "first to be or not to be top"
data = data.split()
for word in data:
    s.push(word)
print(s)
print(s.pop())
print(s)


class Queue:

    def __init__(self):
        self.first = Node(None)
        self.last = Node(None)
        self.n = 0

    def __sizeof__(self):
        return self.n

    def enqueue(self, data):
        temp = self.last
        self.last=Node(data)
        if self.is_empty():
            self.first=self.last
        else:
            temp.link=self.last
        self.n+=1


    def __str__(self):
        item = self.first
        count = 0
        result = ""
        while item.link is not None:
            result += f"Node {count}: {item.data,item.link}\n"
            count += 1
            item = item.link
        return result

    def dequeue(self):
        result = self.first.data
        self.first = self.first.link
        self.n -= 1
        return result

    def is_empty(self):
        return self.n == 0


print("-" * 100 + "Queue" + "-" * 100)
q = Queue()

for i in range(100):
    q.enqueue(i)
while not q.is_empty():
    print(q.dequeue())
