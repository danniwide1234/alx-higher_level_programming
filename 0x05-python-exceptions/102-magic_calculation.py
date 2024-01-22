#!/usr/bin/python3
def magic_calculation(a, b):
    expression = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
            expression += a ** b / m
        except Exception:
            expression = b + a
            break
    return expression
