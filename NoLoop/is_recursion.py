from bdb import Bdb
import sys
import os
from traceback import print_tb

# Based on code of Alex Hall via Stackoverflow
# Modidfied to utilize general execution rather than method call
# as well as incorporating codepost test syntax 
# (yes it uses import to run the code, don't make me explain why you need to do that)

class RecursionDetected(Exception):
    pass

class RecursionDetector(Bdb):
    def do_clear(self, arg):
        pass

    def __init__(self, *args):
        Bdb.__init__(self, *args)
        self.stack = set()

    def user_call(self, frame, argument_list):
        code = frame.f_code
        if code in self.stack:
            raise RecursionDetected
        self.stack.add(code)

    def user_return(self, frame, return_value):
        self.stack.remove(frame.f_code)

def test_recursion():
    detector = RecursionDetector()
    detector.set_trace()
    try:
        sys.argv = ["no_loop.py", "10"]
        import no_loop
          

    except RecursionDetected:
        return True
    else:
        return False
    finally:
        sys.settrace(None)

def TestCase():
    if test_recursion():
        return TestOutput(passed=True, logs="Recursion detected.")
    else:
        return TestOutput(passed=False, logs="Recursion not detected.")