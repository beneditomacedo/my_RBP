#!/usr/bin/env python3
""" Tetranucleotide frequency """

import argparse
import os
from typing import NamedTuple, Tuple


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
def count(args: Args) -> Tuple[int, int, int, int]:
    """ Count DNA bases """
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for base in args.dna:
        if base not in counts:
            counts[base] = 0
        counts[base] += 1

    return (counts.get('A', 0), counts.get('C', 0),
            counts.get('G', 0), counts.get('T', 0))


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    counts = count(args)

    print('{} {} {} {}'.format(*counts))  # splat a tuple


# --------------------------------------------------
if __name__ == '__main__':
    main()
