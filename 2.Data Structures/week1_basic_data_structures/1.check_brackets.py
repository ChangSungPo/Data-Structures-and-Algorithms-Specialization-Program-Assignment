# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            bracket = Bracket(next, i)
            opening_brackets_stack.append(bracket)
            pass

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            tmp = opening_brackets_stack.pop()
            if are_matching(tmp.char,next):
                pass
            else:
                return i+1
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0].position + 1
    return "Success"

def main():
    text = input()
    # text = "{[}"
    mismatch = find_mismatch(text)
    print(mismatch)
    


if __name__ == "__main__":
    main()
