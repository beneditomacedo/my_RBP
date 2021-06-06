#!/usr/bin/env python3
""" Tetranucleotide frequency """

import argparse
import os
from typing import NamedTuple, Dict
from collections import defaultdict


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='DNA', help='Input DNA sequence')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def count(args: Args) -> Dict[str, int]:
    """ Count DNA bases """
    counts = defaultdict(int)

    for base in args.dna:
        if base not in counts:
            counts[base] = 0
        counts[base] += 1

    return counts


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    counts = count(args)

    print('{} {} {} {}'.format(counts['A'], counts['C'],
                               counts['G'], counts['T']))


# --------------------------------------------------
if __name__ == '__main__':
    main()
