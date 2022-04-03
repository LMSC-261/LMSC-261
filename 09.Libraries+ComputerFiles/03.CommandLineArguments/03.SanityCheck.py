import sys

if len(argv) < 2:
  print('usage: python sys.argv[0] [integers]...')
  exit()

sum = 0

# Use 1: slicing to exclude the file name
for number in sys.argv[1:]:
  sum += int(number)

print(sum)