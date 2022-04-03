#---------------------------------------------
# The for statement systax
# for Index in range(StopAt):
#  Code to run until the Index reaches StopAt

for i in range(128):
  print(f"The next MIDI note value is {i}")

# Decrement Instead
for i in range(127, -1, -1):
  print(f"The next MIDI note value is {i}")

# Increment by 2
for i in range(0, 128, 2):
  print(f"The next MIDI note value is {i}")