from random import randrange
import random

import subprocess

def TestCase():
    all_working = False
    for x in range(0, 100):
        i=randrange(0, 9999999)
        b=randrange(0, 9999999)
        vals=[str(i),str(b),str(i)]
        random.shuffle(vals)
        istr=["python3", "all_equal.py"]
        istr= istr+vals
        proc = subprocess.Popen(istr, stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        out = str(out)[2:len(out)+1]
        if "two equal"==out:
            all_working = True
        else:
            all_working = False
            break

    log=test_log("100 Random inputs, 2 same 1 different", all_working, vals, "two equal", out)
    if all_working:
        return TestOutput(passed=True, logs=log)
    else:
        return TestOutput(passed=False, logs=log)

def test_log(testname, passed, input,expected,got):
    result="Passed" if passed else "Failed"
    return_string=""
    return_string+=("Testing " + testname + ": " + result+ "\n")
    return_string+=("=========="+ "\n")
    if not passed:
        return_string+=("Input: " + str(input)+ "\n")
        return_string+=("=========="+ "\n")
        return_string+=("Expected: " + expected+ "\n")
        return_string+=("=========="+ "\n")
        return_string+=("Got: " + got+ "\n")
        return_string+=("=========="+ "\n")
    return return_string