# doctest from run_docstring_examples

from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

# unittest

def add(a,b):
    return a+b
from unittest import TestCase


class TestExample(TestCase):

    def test_add(self):
        result = add(2,2)
        self.assertEqual(result, 100)

import unittest

def run_unittest():
    unittest.main(argv=[''], verbosity=0, exit=False)

run_unittest()