add_library('sound')

soundfile = None

def setup():
    global soundfile
    size(640, 360)
    background(255)
    soundfile = SoundFile(this, "vibraphon.aiff")
    soundfile.loop()
    
def draw():
    global soundfile
    playbackSpeed = map(mouseY, 0, height, 4.0, 0.25)
    soundfile.rate(playbackSpeed)

    panning = map(mouseX, 0, width, -1.0, 1.0)
    soundfile.pan(panning)
