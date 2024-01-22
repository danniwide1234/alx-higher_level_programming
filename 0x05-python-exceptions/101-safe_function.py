#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        expression = fct(*args)
    except Exception as d:
        sys.stderr.write("Exception: {}\n".format(d))
        expression = None

    return (expression)
