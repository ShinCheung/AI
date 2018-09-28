import sys

for line in sys.stdin:
    line = line.strip().split()
    for item in line:
        print(item, 1)
