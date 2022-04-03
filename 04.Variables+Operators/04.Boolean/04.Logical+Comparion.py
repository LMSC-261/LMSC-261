# Declare variables a, b, and result
a = 10
b = 20
result = False

# Is a greater than or less than b?
result = a > b or a < b
print("a is greater than or less than b.", result)

# Is a greater than and less than b?
result = a > b and a < b
print("a is greater than and less than b.", result)

# Is a greater than and not less than b?
result = a > b and not (a < b)
print("a is greater than and not less than b.", result)