import unittest

from malta.factory import Factory


class TestEnvironment(unittest.TestCase):

    # def test1(self):
    #     e = Environment()

    def test_save(self):

        fname = 'out/environment_example.dot'

        e = Factory.get_environment1()
        e.save_as_dot_digraph(fname)
