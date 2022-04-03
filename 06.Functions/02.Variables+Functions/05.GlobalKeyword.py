name = input("What is your name? ")

def display_name():
  global name
  print("Your name is: ", name)
  name = input(f"Are you sure your name is {name}? ")
  print(name)

display_name()
