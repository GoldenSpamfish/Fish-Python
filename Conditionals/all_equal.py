import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == b and b == c:
    print("all equal")
elif a == b or a == c or b == c:
    print("two equal")
else:
    print("all different")