import sys

line_count = 0

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if not sys.argv[1].endswith('.py'):
    print("Not a Python file")
    sys.exit(1)

with open(str(sys.argv[1]), 'r') as file:
    try:
        for line in file:
            line = line.lstrip()
            if line.startswith('#') or not line.strip():
                continue
            else:
                line_count += 1
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

print(line_count)