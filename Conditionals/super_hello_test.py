# To call a student's method, uncomment the following line and call <fileName>.<method>

from random import randrange
import subprocess

def working(n):
    accum=""
    for _ in range(n):
            accum += "Hello!" + "\\n"
    return accum

def TestCase():
    all_working = False
    for _ in range(0, 10):
        i=randrange(0, 99)
        istr=str(i)
        proc = subprocess.Popen(["python3", "super_hello.py", istr], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        out = str(out)[2:-1]
        if working(i)==out:
            all_working = True
        else:
            all_working = False
            break

    log=test_log("Print \"Hello!\" a random number of times, 10 times", all_working, i, working(i), out)
    if all_working:
        return TestOutput(passed=True, logs=log)
    else:
        return TestOutput(passed=False, logs=log)

def test_log(testname, passed, input,expected,got):
    if "\\n" in expected:
        expected = " ".join(expected.split("\\n"))
    if "\\n" in got:
        got = " ".join(got.split("\\n"))
    result="Passed" if passed else "Failed"
    return_string=""
    return_string+=("Testing " + testname + ": " + result+ "\n")
    return_string+=("=========="+ "\n")
    if not passed:
        return_string+=("Input: " + str(input)+ "\n")
        return_string+=("=========="+ "\n")
        return_string+=("Expected: " + expected+ "\n")
        return_string+=("=========="+ "\n")
        return_string+=("Got: " + got + "\n")
        return_string+=("=========="+ "\n")
    return return_string