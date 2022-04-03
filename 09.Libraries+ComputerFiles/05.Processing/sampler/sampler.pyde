add_library('sound')

filenames = ['BD', 'CB', 'CH', 'CHH', 'CY', 'HC', 'HT', 'LT', 'MT', 'OH', 'RS', 'SN']
trigger = millis()
file = []
play = []
  
def setup():
  size(640, 360)
  background(255)

  for filename in filenames:
    file.append(SoundFile(this, filename + ".wav"))
    play.append(int(random(0, 2)))
    
  trigger = millis()

def draw():
    global trigger
    if millis() > trigger:
        background(255)

        for i in range(len(filenames)):      
            if play[i] == 1:
                fill(int(random(255)), int(random(255)), int(random(255)))
                noStroke()
                rect(width / len(filenames) * i, 50, width / len(filenames), 260)
                file[i].play(1.0, 1.0)
        
            play[i] = int(random(0, 2))

        trigger = millis() + int(random(200, 500))
