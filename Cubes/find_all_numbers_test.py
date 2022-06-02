# To call a student's method, uncomment the following line and call <fileName>.<method>

from random import randrange
import subprocess

#REQUIRES ADAPTATION (new function body)
def working(n):
    accum=""
    # find the cube root of `n`
    cb = int(pow(n, 1.0 / 3))
 
    # create an empty set
    s = set()
 
    for i in range(1, cb - 1):
        for j in range(i + 1, cb + 1):
 
            # (i, j) forms a pair
            sum = (i*i*i) + (j*j*j)
 
            # sum is seen before
            if sum in s:
                accum += str(sum) + "\\n"
            else:
                # sum is not seen before
                s.add(sum)
    return accum

def TestCase():
    all_working = False
    #MAY REQUIRE ADAPTATION (ranges)
    for _ in range(0, 10):
        i=randrange(0, 999999)
        istr=str(i)
        #REQUIRES ADAPTATION (name of the file)
        proc = subprocess.Popen(["python3", "find_all_numbers.py", istr], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        out = str(out)[2:-1]
        if working(i)==out:
            all_working = True
        else:
            all_working = False
            break
    #REQUIRES ADAPTATION (name of the test)
    log=test_log("Print numbers not greater than n with 2 factorial pairs for 10 random n", all_working, i, working(i), out)
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