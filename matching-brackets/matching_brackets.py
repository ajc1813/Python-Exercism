
brackets = {"(": ")", "[": "]", "{": "}"}
def is_paired(input_string):
    stack = []
    for c in input_string:
        if c in brackets.keys():
            stack.append(brackets[c])
        elif c in brackets.values():
            if len(stack)==0 or c != stack.pop():
                return False
    return not stack