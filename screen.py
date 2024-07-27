import os
import array
import consts

def clamp(val, min, max):
    return max if val > max else (min if val < min else val)

class Screen:
    def __init__(self):
        self.pixels = array.array('d', [0] * consts.NUMBER_OF_PIXELS)
        self.fill(' ')

    def display(self):
        os.system("cls")
        print(self.buffer, end="", flush=True)
    
    def fill(self, c):
        self.buffer = (c * (consts.WIDTH) + '\n') * consts.HEIGHT;

    def charFromBrightness(self, bright):
        bright = clamp(bright, 0.0, 1.0)
        bright *= len(consts.GRAY_SCALE) - 1;
        return consts.GRAY_SCALE[round(bright)]

    def calcChar(self, x, y):
        value = 0.0
        
        x *= consts.CHAR_WIDTH
        y *= consts.CHAR_HEIGHT

        for pixelY in range(consts.CHAR_HEIGHT):
            for pixelX in range(consts.CHAR_WIDTH):
                value += self.getPixel(pixelX + x , pixelY + y)
        
        value /= consts.PIXELS_PER_CHAR
        return self.charFromBrightness(value)

    def update(self):
        self.buffer = ""
        for y in range(consts.HEIGHT):
            for x in range(consts.WIDTH):
                self.buffer += self.calcChar(x, y)
            self.buffer += '\n'
    
    def pixelIndex(self, x: int, y: int):
        if (x < 0 or x >= consts.PIXEL_WIDTH or y < 0 or y >= consts.PIXEL_HEIGHT):
            return None
        return x + y * consts.PIXEL_WIDTH
    
    def getPixel(self, x: int, y: int):
        index = self.pixelIndex(x, y)
        return None if index == None else self.pixels[index]
    def setPixel(self, x: int, y: int, val: float):
        index = self.pixelIndex(x, y)
        if index != None:
            self.pixels[index] = val