# To call a student's method, uncomment the following line and call <fileName>.<method>

from random import randrange
import subprocess
from unittest import result

def working_primetest(x):
    if x == 0:
        return "False"
    for i in range(1, x):
        if (x / i) % 1 == 0 and x != i and i != 1:
            return "False"
    else:
        return "True"

def TestCase():
    all_working = False
    #print("number   yours   working")
    for x in range(0, 10):
        i=randrange(0, 9999999)
        istr=str(i)
        proc = subprocess.Popen(["python3", "isPrime.py", istr], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        out = str(out)[2:len(out)+1]
        #print(str(i) + ":  "+ out + "  " + working_primetest(i))
        if working_primetest(i)==out:
            all_working = True
        else:
            all_working = False
            break

    if all_working:
        return TestOutput(passed=True, logs="Works with all 10 random primes")
    else:
        return TestOutput(passed=False, logs= testLog("10 Random Primes", all_working, i, working_primetest(i), out))

def testLog(testname, passed, input,expected,got):
    result="Passed" if passed else "Failed"
    exptype="Prime" if expected=="True" else "Not Prime"
    gottype="Prime" if got=="True" else "Not Prime"
    return_string=""
    return_string+=("Testing " + testname + ": " + result+ "\n")
    return_string+=("=========="+ "\n")
    return_string+=("Input: " + str(input)+ "\n")
    return_string+=("=========="+ "\n")
    return_string+=("Expected: " + exptype+ "\n")
    return_string+=("=========="+ "\n")
    return_string+=("Got: " + gottype+ "\n")
    return_string+=("=========="+ "\n")
    return return_string