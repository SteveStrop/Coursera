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
        self.root = self.__put__(self.root, k, v)

    def get(self, k):
        return self.__get__(self.root, k)

    def min(self):
        return self.__min__(self.root)

    def max(self):
        return self.__max__(self.root)

    def __min__(self, root):
        if root.left is None:
            return root.value
        else:
            return self.__min__(root.left)

    def __max__(self, root):
        if root.right is None:
            return root.value
        else:
            return self.__max__(root.right)

    def __put__(self, new_node, k, v):
        if new_node is None:
            return Node(k, v)

        if k > new_node.key:
            new_node.right = self.__put__(new_node.right, k, v)
        elif k < new_node.key:
            new_node.left = self.__put__(new_node.left, k, v)
        else:
            new_node.value = v
        return new_node

    def __get__(self, node, k):
        if node is None:
            return None
        if k > node.key:
            return self.__get__(node.right, k)
        elif k < node.key:
            return self.__get__(node.left, k)
        else:
            return node.value


b = BST()
b.put(2, "two")
b.put(4, "four")
b.put(3, "three")
b.put(1, "one")


print(b.get(5))
print(b.get(3))
print(b.min())
print(b.max())
b.put(3,"seventy nine")
print(b.get(3))
