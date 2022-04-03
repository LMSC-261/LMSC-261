# Infinite while loop where we forgot to update the value of midiNote
# to meet the stopping condition.

midiNote = 64

while midiNote <= 76:
  print(f"MIDI note is {midiNote}")