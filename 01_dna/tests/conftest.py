""" Tests configuration for dna.py

The pytest tests running from command line was running properly but when it
was running from vscode the tests were failling.
Apparentenly because the working directory was wrong. So this file was
created to fix this problem.

"""
import os

HOME_PROJECT = '/Users/beneditomacedo/BioInfo/RBP/01_dna'


def pytest_sessionstart(session):
    os.chdir(HOME_PROJECT)
