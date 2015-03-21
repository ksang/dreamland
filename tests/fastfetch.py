import unittest
import random
import time
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
            v = random.randrange(0,10)
            (a, b) = (v, v)
            print "Inserting new value: (%s, %s)" % (a, b)
            stack.touch((a,b), "Value")
            self.print_status(stack)
        stack.get(stack.pos[0])
        print "After get last element:"
        self.print_status(stack)
        print "Getting 3rd most recent element"
        print stack.inspect(3)

    def test_b_vitalize(self):
        stack = FastFetch(10,5)
        for i in range(0,10):
            v = random.randrange(0,10)
            stack.touch((v,v), "Value")
        self.print_status(stack)
        print "After vitalize, size:%s, gate:%s" %(10,5)
        stack.vitalize()
        self.print_status(stack)

    def test_c_big_land(self):
        start = time.time()
        stack = FastFetch(100000,50000)
        for i in range(0,150000):
            (a,b) = (random.randrange(0,100000), random.randrange(0,100000))
            stack.touch((a,b), "Value")
        print "Insert complete, time used: %s checking correstness:" % str(time.time() - start)
        print "DATA_STORE size: %s position list size: %s" %(len(stack.DATA_STORE), len(stack.pos))
        for key in stack.pos:
            if stack.DATA_STORE.get(key) is None:
                print "Inconsistant: %s" % key
        start2 = time.time()
        stack.vitalize()
        print "Vitalize complete, time used: %s" % str(time.time() - start2)
        print "DATA_STORE size: %s position list size: %s" %(len(stack.DATA_STORE), len(stack.pos))