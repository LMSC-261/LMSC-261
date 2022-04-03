midiNote = 64

#---------------------------------------------
# Nested if statement
  
if midiNote < 64:
  print("MIDI note is smaller than 64.")
  if midiNote == 48:
    print(f"The note name for {midiNote} is C2.")
  elif midiNote == 40:
    print(f"The note name for {midiNote} is E1.")
else:
  print("MIDI note is greater than or equal to 64.")