import sys
x=int(sys.argv[1])

if x <= 0:
    print(False)
else:
    prime=True
    for i in range(1, x):
        if (x / i) % 1 == 0 and x != i and i != 1:
            prime=False
            print("False")
            break
    if prime:
        print("True")