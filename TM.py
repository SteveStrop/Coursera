"""
Sample data file (binary add):\n
6  2                     (number of states N , start state)\n
10+#                    (alphabet)\n
L 1 0 4 0 0 1 # #       (state N transitions then N outputs per letter)\n
L 1 1 3 1 1 0 + #\n
R 2 2 2 0 1 0 + #\n
L 3 2 3 2 0 1 + 1\n
R 4 4 4 5 # 0 + #\n
H 5 5 5 5 1 0 + #\n

"""

from Linked_Lists import Stack


action = []
transition = []
output = []

with open("TM.txt", "r")as f:
    state_count, state = map(int, f.readline().split())
    alphabet = f.readline().rstrip("\n")
    alpha_count = len(alphabet)
    for _ in range(state_count):
        data = f.readline().rstrip("\n").split()
        action.append(data[0])
        t = {alphabet[i]: int(data[i + 1]) for i in range(alpha_count)}
        o = {alphabet[i]: data[i + alpha_count + 1] for i in range(alpha_count)}  # alpha_count is offset to output
        output.append(o)


def print_machine_defn():
    print(f"Stages: {state_count}")
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
