import sys

if len(sys.argv) != 2:
    print("Usage: python add_funny.py 'Your funny thing here'")
    sys.exit(1)

funny_thing = sys.argv[1]

with open('funny.txt', 'a') as f:
    f.write(funny_thing + '\n')

print(f"Successfully added '{funny_thing}' to funny.txt")
