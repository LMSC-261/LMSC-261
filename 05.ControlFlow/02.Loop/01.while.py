midiNote = 64
#---------------------------------------------
# The while statement systax
# while BooleanExpression:
#  Code to run until BooleanExpression becomes False

# while loop that increments MIDI note until note value 77 is reached
while midiNote <= 76:
  print(f"MIDI note is {midiNote}")
  midiNote += 1