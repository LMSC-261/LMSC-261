# Execute this file with:
# python3 1.argv.py 860 1190 1460
import sys
sum = 0

# Use 1: slicing to exclude the file name
for number in sys.argv[1:]:
  sum += int(number)

print(sum)