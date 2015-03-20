#!/usr/bin/python
import sys, types
import unittest

from tests.fastfetch import TestFastFetch

test_cases = [  TestFastFetch,
                ]

class Tester:

    def __init__(self, test_cases):
        self.testSuite = unittest.TestSuite()
        for case in test_cases:
            self.testSuite.addTest(unittest.makeSuite(case))

    def run_test(self):
        testRunner = unittest.TextTestRunner()
        testRunner.run(self.testSuite)

def print_usage():
    classes = []
    for ctest in test_cases:
        classes.append(str(ctest).split('.')[-1:][0][:-2])
    print '''
    Usage:      run_tests.py <test_case_1> <test_cases_2> ...
    Test cases: 
                %s
    ''' % str(classes)
    sys.exit(1)

def parse_argv(argv):
    res = []
    for arg in argv:
        try:
            identifier = getattr(sys.modules[__name__], arg)
        except AttributeError:
            print "ERROR: %s doesn't exist." % arg
            print_usage()
        if isinstance(identifier, (types.ClassType, types.TypeType)):
            res.append(identifier)
        else:
            print "ERROR: %s is not a class." % arg
            print_usage()
    return res

if __name__ == "__main__":
    use_cases = []
    if len(sys.argv) > 1:
        use_cases = parse_argv(sys.argv[1:])
    else:
        print_usage()
    tester = Tester(use_cases)
    try:
        tester.run_test()
    except KeyboardInterrupt:
        print 'Operation aborted.'
        sys.exit()