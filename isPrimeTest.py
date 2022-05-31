# To call a student's method, uncomment the following line and call <fileName>.<method>

from isPrime import is_prime

def working_primetest(x):
    if x == 0:
        return False
    for i in range(1, x):
        if (x / i) % 1 == 0 and x != i and i != 1:
            return False
    else:
        return True

def TestCase():
    all_working = False
    
    for i in range(0, 10):
        if is_prime(i)==working_primetest(i):
            all_working = True
        else:
            all_working = False
            break

    if all_working:
        return TestOutput(passed=True, logs="Test passed.")
    else:
        return TestOutput(passed=False, logs="Test failed.")