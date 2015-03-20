import unittest
import random
from dreamland import FastFetch

class TestFastFetch(unittest.TestCase):
    def setUp(self):
        pass

    def print_status(self, stack):
        print str(stack.DATA_STORE)
        print str(stack.pos)

    def test_a_small_land(self):
        stack = FastFetch(5)
        for i in range(0,10):
            (a, b) = (random.randrange(0,5), random.randrange(0,5))
            print "Inserting new value: (%s, %s)" % (a, b)
            stack.touch((a,b), "Value")
            self.print_status(stack)
        stack.get(stack.pos[4])
        print "After get last element:"
        self.print_status(stack)