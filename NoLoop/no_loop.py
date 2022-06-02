import sys
x=int(sys.argv[1])
def no_loop(num):
    if (num > 0):
        no_loop(num-1)
        print(num)    
no_loop(x)