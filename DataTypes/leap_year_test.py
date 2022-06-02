# To call a student's method, uncomment the following line and call <fileName>.<method>

from random import randrange
import subprocess

#REQUIRES ADAPTATION (new function body)
# needs to return a string, with /n if multiple lines
def working(year):
    result = year % 4 == 0
    result = result and year % 100 != 0
    result = result or year % 400 == 0
    return str(result)

def TestCase():
    all_working = False
    #MAY REQUIRE ADAPTATION (ranges)
    for _ in range(0, 100):
        i=randrange(0, 99999)
        istr=str(i)
        #REQUIRES ADAPTATION (name of the file)
        proc = subprocess.Popen(["python3", "leap_year.py", istr], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        out = str(out)[2:-1]
        out = out.replace("\\n", "")
        if working(i)==out:
            all_working = True
        else:
            all_working = False
            break
    #REQUIRES ADAPTATION (name of the test)
    log=test_log("100 Random years", all_working, i, working(i), out)
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