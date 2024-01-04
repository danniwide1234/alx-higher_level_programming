#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    expression = 0
    for x in sys.argv:
        if x != sys.argv[0]:
            expression += int(x)
    print(expression)
