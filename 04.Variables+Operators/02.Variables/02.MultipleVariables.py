# Create multiple vairables and assign different values
x, y, z = 1, 2, 3
print(x, y, z)

# Create multiple variables and assign one value
x = y = z = 1
print(x, y, z)

# Cannot insert an arithmetic operator in between assignment operators
# Python will throw a syntax error
# x = y + 1 = z = 1