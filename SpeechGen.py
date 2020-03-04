import numpy as np

with open("tw", "r") as myfile:  # importing the file
    data = myfile.read()

s = """"""  # alternatively, type it here

s = data


# s = " ".join(s)

def token(string):
    start = 0
    i = 0
    token_list = []
    for x in range(0, len(string)):
        if " " == string[i:i + 1][0]:
            # trimming out commas and spaces
            token_list.append(
                (string[start:i + 1]).replace(" ", ""))
            start = i + 1
        i += 1
    token_list.append(string[start:i + 1])
    return token_list


def build_transition_matrix(c):
    corpus = c
    transitions = {}
    for k in range(0, len(corpus)):
        word = corpus[k]
        if k != len(corpus) - 1:  # Deal with last word
            next_word = corpus[k + 1]
        else:
            next_word = corpus[0]  # To loop back to the beginning

        if word not in transitions:
            transitions[word] = []

        transitions[word].append(next_word)
    return transitions


transition_matrix = token(s)

lst = build_transition_matrix(transition_matrix)

print(lst)

current_word = np.random.choice(transition_matrix)

sentence = []

for k in range(0, 200):  # number of words in the sentence
    # add current word to the sentence
    if current_word == ",":
        sentence.append(current_word)
    else:
        sentence.append(" " + current_word)
    # get holder for the list of finding the current entry in the dictionary
    holder = lst[current_word]
    # changing the current word
    current_word = np.random.choice(holder)

' '.join(sentence)

output = "".join(sentence)
print("TEXT GENERATION BEGINS HERE" + "\n")
print(output[1:len(output)])
