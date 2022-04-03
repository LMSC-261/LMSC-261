midiNote = 64
#---------------------------------------------
# The while statement systax
# while BooleanExpression:
#  Code to run until BooleanExpression becomes False
# else:
#  Code to run when BooelanExpression becomes False

# while-else loop that increments MIDI note until note value 77 is reached
# The loop exits after executing the code in the else statement
while midiNote <= 76:
  print(f"MIDI note is {midiNote}")
  midiNote += 1
else:
  print(f"The last MIDI note is {midiNote}")