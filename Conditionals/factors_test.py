# To call a student's method, uncomment the following line and call <fileName>.<method>

from random import randrange
import subprocess

def working(n):
    accum=""
    i = 1
    while i <= n:
        if n % i == 0:
            accum += str(i) + "\\n"
        i += 1
    return accum

def TestCase():
    all_working = False
    for x in range(0, 10):
        i=randrange(0, 9999999)
        istr=str(i)
        proc = subprocess.Popen(["python3", "factors.py", istr], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        out = str(out)[2:-1]
        if working(i)==out:
            all_working = True
        else:
            all_working = False
            break

    log=test_log("Factor 100 random integers", all_working, i, working(i), out)
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