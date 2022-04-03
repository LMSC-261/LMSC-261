# create a variable and change its type later
string = 6
string = 'Hello, String!'
print(string)

# We cannot write an expression between a number and string
#pi = "PI: " + 3.14

# If we want to stitch the two, we need to use str()
pi = "PI: " + str(3.14)
print(pi)