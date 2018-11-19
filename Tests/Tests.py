from unittest import TestCase
import random

from algos import three_sum_bin
from Linked_Lists import Queue,Stack


class Tests(TestCase):
    def test_3_sum(self):
        random.seed(900)
        a = [random.randint(-100000, 100000) for _ in range(1000)]
        a = sorted(list(set(a)))
        self.assertEqual(586,three_sum_bin(a))

    def test_queue(self):
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

    def test_stack(self):
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

