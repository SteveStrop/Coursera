from Linked_Lists import Stack


class TM:

    def __init__(self):
        self.tape = Tape()
        # initialised in mount
        self.calc = None
        # initialised in load_machine
        self.state_count = None
        self.alphabet = None
        self.actions = None
        self.transitions = None
        self.outputs = None
        self.initial_state = None


    def mount(self, calc):
        """Mount a tape into the turing machine"""
        self.calc = calc
        self.tape.load(self.calc)

    def load_machine(self, file):
        """ Read a turing machine specification from a file.

        Sample data file (binary add):
        6  2                     (number of states N , start initial_state)\n
        10+#                    (alphabet)\n
        L 1 0 4 0 0 1 # #       (initial_state N transitions then N outputs per letter)\n
        L 1 1 3 1 1 0 + #\n
        R 2 2 2 0 1 0 + #\n
        L 3 2 3 2 0 1 + 1\n
        R 4 4 4 5 # 0 + #\n
        H 5 5 5 5 1 0 + #\n

        """
        self.actions = []  # list of all state actions
        self.transitions = []  # list of transitions from one state to another
        self.outputs = []  # list of outputs corresponding to each transitions

        with open(file, "r")as f:
            self.state_count, self.initial_state = map(int, f.readline().split())
            self.alphabet = f.readline().rstrip("\n")
            alpha_count = len(self.alphabet)
            for _ in range(self.state_count):
                data = f.readline().rstrip("\n").split()
                # save state type (L)eft, (R)ight, (H)alt
                self.actions.append(data[0])
                # create dict of transitions for this state (transitions start at position 1 in data list)
                t = {self.alphabet[i]: int(data[i + 1]) for i in range(alpha_count)}
                # create dict of outputs for this state (outputs start at position alpha_count +1 in data list)
                o = {self.alphabet[i]: data[i + alpha_count + 1] for i in range(alpha_count)}
                # add this states transitions and outputs to the master lists
                self.transitions.append(t)
                self.outputs.append(o)

    def print_machine_defn(self):
        """ Print out specification of loaded machine."""
        print(f"States: {self.state_count}")
        print(f"Alphabet: {self.alphabet}")
        print(f"Actions: {self.actions}")
        print(f"Outputs: {self.outputs}")
        print(f"Transitions: {self.transitions}")

    def run(self):
        state = self.initial_state
        while self.actions[state] != "H":
            inpt = self.tape.read()
            self.tape.write(self.outputs[state][inpt])
            state = self.transitions[state][inpt]
            if self.actions[state] == "L":
                self.tape.move_left()
            elif self.actions[state] == "R":
                self.tape.move_right()
        self.print_result()

    def print_result(self):
        print(self.calc, "=", self.tape.read_tape())


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


tm = TM()
tm.load_machine("binary_add.txt")
tm.mount("1110+1")
tm.run()
