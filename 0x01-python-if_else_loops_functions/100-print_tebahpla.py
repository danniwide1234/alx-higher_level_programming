#!/usr/bin/python3
for rev in reversed(range(97, 123)):
    print("{:c}".format(rev if (rev % 2 == 0) else (rev - 32)), end='')
