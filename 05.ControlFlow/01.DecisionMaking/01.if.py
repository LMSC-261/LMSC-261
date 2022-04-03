midiNote = 64

#---------------------------------------------
# The if statement systax
# if BooleanExpression:
#  Code to run when BooleanExpression is True

# Print a message, if MIDI note is is out of range
if midiNote < 0 or midiNote > 127:
  print("\nThe note value entered is an invalid MIDI note.\n")

if midiNote >= 0 and midiNote <= 127:
  print("The note value entered is a valid MIDI note.")
  print("MIDI note value is", midiNote)