def TestCase():
    f = open('no_loop.py', 'r')
    content=f.read()
    content=content.split()
    for i in content:
        if (i == 'for' or i == 'while'):
            return TestOutput(passed=False, logs="Test failed.")  
    return TestOutput(passed=True, logs="Test passed.")