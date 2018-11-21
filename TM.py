from Linked_Lists import Stack

with open("TM.txt", "r")as f:
    stages = int(f.readline())
    alphabet = f.readline().rstrip("\n")
    key_count = len(alphabet)
    action = []
    transition = []
    output = []

    for _ in range(stages):
        t = {}
        o = {}
        data = f.readline().rstrip("\n").split()
        action.append(data[0])
        for i in range(key_count):
            t[alphabet[i]] = int(data[i + 1])
            o[alphabet[i]] = data[i + key_count + 1]
        transition.append(t)
        output.append(o)


def print_machine_defn():
    print(f"Stages: {stages}")
    print(f"Alphabet: {alphabet}")
    print(f"Actions: {action}")
    print(f"Outputs: {output}")
    print(f"Transitions: {transition}")


# print_machine_defn()


class Tape:
    """ Implement a Turing machine input tape interface using two stacks"""

    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def move_left(self):
        self.right.push(self.left.pop())

    def move_right(self):
        self.left.push(self.right.pop())

    def read(self):
        char = self.right.peek()
        return char is None and "#" or char

    def write(self, char):
        self.right.pop()
        self.right.push(char)

    def load(self, tape):
        tape = tape[::-1]
        for char in tape:
            self.right.push(char)

    def read_tape(self):
        result = ""
        while not self.left.is_empty():
            self.right.push(self.left.pop())
        while not self.right.is_empty():
            result += self.right.pop()
        return result.strip("#")


test_string = "1110+1"
numbers = test_string.split("+")

t = Tape()
t.load(test_string)
state = 2
while action[state] != "H":
    inpt = t.read()
    t.write(output[state][inpt])
    state = transition[state][inpt]
    if action[state] == "L":
        t.move_left()
    elif action[state] == "R":
        t.move_right()
answer = t.read_tape()
print(int(numbers[0], 2), "+", int(numbers[1], 2), "=", int(answer, 2))
print(f"{test_string} = {answer}")
