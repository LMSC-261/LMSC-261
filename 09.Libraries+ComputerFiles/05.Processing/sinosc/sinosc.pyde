add_library('sound')

sine = SinOsc(this)

def setup():
  size(640, 360)
  background(255)

  sine.play()

def draw():
    freq = map(mouseX, 0, width, 220, 1760)
    sine.freq(freq)
    
    amp = map(mouseY, 0, height, 1.0, 0.0)
    sine.amp(amp)
