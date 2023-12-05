from PIL import ImageGrab
import mouse


for i in range(0,1):
    found = False
    skjerm = ImageGrab.grab()
    targetColor = skjerm.getpixel((740,1800))
      
    for y in reversed(range(0, 2000, 1)):
        if y < 1700:
            for x in (range(0, 1500, 1)):
                if found == False:      
                    color = skjerm.getpixel((x, y))
                    #print(color)
                    if color == targetColor:
                        found = True
                        print(f"Fargen befinner seg på {x} og {y}")
                        curPos = mouse.get_position()
                        mouse.move(x-curPos[0], y-curPos[1], absolute=False, duration=0.5)
