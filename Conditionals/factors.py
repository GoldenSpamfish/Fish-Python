import sys
n = int(sys.argv[1])

i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1