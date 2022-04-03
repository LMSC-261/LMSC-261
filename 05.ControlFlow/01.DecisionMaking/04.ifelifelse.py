midiNote = 64

#---------------------------------------------
# The if-elif-else statement systax
# if BooleanExpression:
#  Code to run when BooleanExpression for if is True
# elif BooleanExpression:
#  Code to run when BooleanExpression for elif is True
# else:
#  Code to run when BooleanExpression is False
  
if midiNote < 64:
  print("MIDI note is smaller than 64.")
elif midiNote > 64:
  print("MIDI note is greater than 64.")
else:
  print("MIDI note is equal to 64.")