import unittest
import random
import time
from dreamland import LRUCache

class TestLRUCache(unittest.TestCase):

    def setUp(self):
        print '\n'
        print '='*64

    def print_node(self, node):
        return "Node: %s \n\tkey: %s, value: %s, \n\tprev: %s, \n\tnext: %s" \
                    % (node, node.key, node.value, node.prev, node.next)

    def print_link_list(self, head):
        node = head
        while node is not None:
            print self.print_node(node)
            node = node.next

    def test_a_small_land(self):
        stack = LRUCache(3)
        data = [(1,1),(2,2),(3,3),(4,4)]
        for d in data:
            stack.touch(d[0],d[1])
        self.print_link_list(stack.head)

    def test_b_big_land(self):
        start = time.time()
        stack = LRUCache(100000)
        for i in range(0,150000):
            (a,b) = (random.randrange(0,100000), random.randrange(0,100000))
            stack.touch((a,b), "Value")
        print "Insert complete, time used: %s checking correstness:" % str(time.time() - start)
        print "Mapping size: %s" % len(stack.mapping)
        node = stack.head
        count = 0
        while True:
            count += 1
            if stack.mapping.get(node.key) is None:
                print "Inconsistant: %s" % key
            if node.next is not None:
                if node != node.next.prev:
                    print "Node pointer mismatch:\n\t%s\n\t%s" \
                            % (self.print_node(node), self.print_node(node.next))
                node = node.next
            else: break
        print "Data check complete, count: %s" % count

    def tearDown(self):
        print '='*64