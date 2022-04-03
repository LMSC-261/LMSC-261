# Use the `while` keyword to create a loop in Python.
# The `while` keyword requires : (colon) at the end on line.
# The line after the : needs to be indented.
# Every indented lines after : will be looped by the `while` loop.

while True:
  print("hello, world")

# Use the `for` keyword to create a loop the repeats a number of times.
# The `for` keyword also requires : (colon) at the end.
# Every indented line after :  will be looped.
# The `for` keyword requires condition to tell computer went to stop.
# The expression begins with declaring an iterating variable (in this case `index`)
# We then tell ‘for’ loop when should it end using the `range()` keyword.
# `range()` tells ‘for’ loop the maximum number `index` should increment to.
# By putting number 10 in the parenthesis, the ‘for’ loop now knows when to stop.
for index in range(10):
  print("hello, world")