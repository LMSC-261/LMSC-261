# Declare two variables x and y
x = 2
y = 10

# If condition in Python
# Notice that in Python, we use { and } (as well as indentation) 
# to indicate how lines of code should be nested. 
if x < y: 
  print("x is less than y")

# If-else condition in code
if x < y:
  print("x is less than y")
else:
  print("x is not less than y")

# Nest if-else condition
if x < y:
  print("x is less than y")
elif x > y:
  print("x is greater than y")
elif x == y:
  print("x is equal to y")

# The last comparison is redundant
# So we can shorten our code just
# saying "else"
if x < y:
  print("x is less than y")
elif x > y:
  print("x is greater than y")
else:
  print("x is equal to y")