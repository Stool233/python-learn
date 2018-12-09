import os

from collections import Counter

import click


@click.command()
@click.option("--count", default=10, help="Number of commands.")
def find_common_used_command(count):

    c = Counter()

    with open(os.path.expanduser('~/.bash_history')) as f:
        for line in f:
            cmd = line.strip().split()
            if cmd:
                c[cmd[0]] += 1

    print(c.most_common(count))


if __name__ == '__main__':
    find_common_used_command()
