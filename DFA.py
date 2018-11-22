"""Parse DFA.txt then run the DFA specified by DFA.txt
DFA.txt must be in the form:
3
10
True 1 0
False 2 1
False 2 0

first line is number of states
second line is alphabet
subsequent lines are result and actions for each state/letter combination

"""

# parse the input data to produce a DFA alphabet, a list of True/False actions for each state and a dictionary of
# operations for each state
with open("DFA.txt", "r")as f:
    stages = int(f.readline())
    alphabet = f.readline().rstrip("\n")
    action, steps = zip(
            *[(data.partition(" ")[0] == "True", data.partition(" ")[-1].split()) for data in f.readlines()])
    next_state = [{letter: int(step[i]) for i, letter in enumerate(alphabet)} for step in steps]

test_string = "110001011101001"
print(f"Checking if {test_string} is in the language")
state = 0
for letter in test_string:
    state = next_state[state][letter]
print(action[state])

print(f"Stages: {state_count}")
print(f"Alphabet: {alphabet}")
print(f"Actions: {action}")
print(f"Transitions: {next_state}")


