def is_prime(x):
    if x == 0:
        return False
    for i in range(1, x):
        if (x / i) % 1 == 0 and x != i and i != 1:
            return False
    else:
        return True


for i in range(-9, 9):
    print(str(i) + str(is_prime(i)))
