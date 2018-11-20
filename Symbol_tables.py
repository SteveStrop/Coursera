class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def put(self, k, v):
        self.root = self.do_put(self.root, k, v)

    def get(self, k):
        return self.do_get(self.root, k)

    def do_put(self, new_node, k, v):
        if new_node is None:
            return Node(k, v)

        if k > new_node.key:
            new_node.right = self.do_put(new_node.right, k, v)
        elif k < new_node.key:
            new_node.left = self.do_put(new_node.left, k, v)
        else:
            new_node.value = v
        return new_node

    def do_get(self, node, k):
        if node is None:
            return None
        if k > node.key:
            return self.do_get(node.right, k)
        elif k < node.key:
            return self.do_get(node.left, k)
        else:
            return node.value


b = BST()
b.put(2, "two")
b.put(4, "four")
b.put(3, "three")
b.put(1, "one")

print(b.get(5))
