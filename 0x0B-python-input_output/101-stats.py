#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Printing accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for ent in sorted(status_codes):
        print("{}: {}".format(ent, status_codes[ent]))


if __name__ == "__main__":
    import sys

    measure = 0
    codes_status = {}
    codes_valid = ['200', '301', '400', '401', '403', '404', '405', '500']
    number = 0

    try:
        for line in sys.stdin:
            if number == 10:
                print_stats(measure, codes_status)
                number = 1
            else:
                number += 1

            line = line.split()

            try:
                measure += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes_valid:
                    if codes_status.get(line[-2], -1) == -1:
                        codes_status[line[-2]] = 1
                    else:
                        codes_status[line[-2]] += 1
            except IndexError:
                pass

        print_stats(measure, codes_status)

    except KeyboardInterrupt:
        print_stats(measure, codes_status)
        raise
