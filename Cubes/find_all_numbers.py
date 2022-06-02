import sys
n=int(sys.argv[1])

def findAllNumbers(n):
 
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
                print(sum)
            else:
                # sum is not seen before
                s.add(sum)

findAllNumbers(n)