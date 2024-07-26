import os
import array
import math

def clamp(val, min, max):
    return max if val > max else (min if val < min else val)

class Screen:
    def __init__(self, width, height, charWidth = 6, charHeight = 13):
        self.width = width
        self.height = height
        self.charWidth = charWidth;
        self.charHeight = charHeight;
        self.pixelWidth = charWidth * width
        self.pixelHeight = charHeight * height
        self.pixelsPerChar = charHeight * charWidth
        self.pixels = array.array('d', [0] * self.pixelWidth * self.pixelHeight)
        self.gradient = " .:!/r(l1Z4H9W8$@"
        self.fill(' ')

    def display(self):
        os.system("cls")
        print(self.buffer, end="", flush=True)
    
    def fill(self, c):
        self.buffer = (c * (self.width) + '\n') * self.height;

    def charFromBrightness(self, bright):
        bright = clamp(bright, 0.0, 1.0)
        bright *= len(self.gradient) - 1;
        return self.gradient[round(bright)]

    def calcChar(self, x, y):
        value = 0.0
        
        x *= self.charWidth
        y *= self.charHeight

        for pixelY in range(self.charHeight):
            for pixelX in range(self.charWidth):
                value += self.pixels[pixelX + x + (pixelY + y) * self.pixelWidth]
        
        value /= self.pixelsPerChar
        return self.charFromBrightness(value)

    def update(self):
        self.buffer = ""
        for y in range(self.height):
            for x in range(self.width):
                self.buffer += self.calcChar(x, y)
            self.buffer += '\n'