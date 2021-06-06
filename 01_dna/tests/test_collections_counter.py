""" Tests for dna_str_count.py """

import os
import platform
from subprocess import getstatusoutput

PRG = './dna_collections_counter.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
TEST1 = ('./tests/inputs/input1.txt', '1 2 3 4')
TEST2 = ('./tests/inputs/input2.txt', '20 12 17 21')
TEST3 = ('./tests/inputs/input3.txt', '196 231 237 246')
TEST4 = ('./tests/inputs/input4.txt', '0 0 0 0')
TEST5 = ('./tests/inputs/input5.txt', '1 0 0 0')
TEST6 = ('./tests/inputs/input6.txt', '0 1 0 0')
TEST7 = ('./tests/inputs/input7.txt', '0 0 1 0')
TEST8 = ('./tests/inputs/input8.txt', '0 0 0 1')


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """
    assert os.path.exists(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Prints usage """

    for arg in ['-h', '--help']:
        rv, out = getstatusoutput(f'{RUN} {arg}')
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_dies_no_args() -> None:
    """ Dies with no arguments """

    rv, out = getstatusoutput(RUN)
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_arg() -> None:
    """ Uses command-line arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        dna = open(file).read()
        retval, out = getstatusoutput(f'{RUN} {dna}')
        assert retval == 0
        assert out == expected


# --------------------------------------------------
def test_file() -> None:
    """ Uses file arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        retval, out = getstatusoutput(f'{RUN} {file}')
        assert retval == 0
        assert out == expected


def test_devnull() -> None:
    """ Test with empty file """

    rv, out = getstatusoutput(f'{RUN} /dev/null')
    assert rv == 0
    assert out == '0 0 0 0'


def test_empty_file() -> None:
    """ Test with empty file """

    rv, out = getstatusoutput(f'{RUN} ./tests/inputs/empty')
    assert rv == 0
    assert out == '0 0 0 0'
