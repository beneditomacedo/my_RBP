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

    count_a = args.dna.count('A')
    count_c = args.dna.count('C')
    count_g = args.dna.count('G')
    count_t = args.dna.count('T')

    return (count_a, count_c, count_g, count_t)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    counts = count(args)

    print('{} {} {} {}'.format(*counts))  # splat a tuple


# --------------------------------------------------
if __name__ == '__main__':
    main()
