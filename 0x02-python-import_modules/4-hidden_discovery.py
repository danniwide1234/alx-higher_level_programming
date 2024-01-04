#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for expression in dir(hidden_4):
        if expression[0] != '_' and expression[1] != '_':
            print(expression)
