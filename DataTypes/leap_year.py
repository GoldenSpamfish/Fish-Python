import sys
year = int(sys.argv[1])

result = year % 4 == 0
result = result and year % 100 != 0
result = result or year % 400 == 0

print(result)