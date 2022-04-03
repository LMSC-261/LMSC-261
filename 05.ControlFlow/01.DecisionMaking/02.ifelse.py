midiNote = 64

#---------------------------------------------
# The if-else statement systax
# if BooleanExpression:
#  Code to run when BooleanExpression is True
# else:
#  Code to run when BooleanExpression is False
  
if midiNote <= 0 or midiNote >= 127:
  print("The note value entered is Invalid.")
else:
  print("The note value entered is valid.")