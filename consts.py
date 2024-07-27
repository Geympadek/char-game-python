WIDTH = 80 #width of the screen in chars
HEIGHT = 10 #height of the screen in chars

CHAR_WIDTH = 6 #width of a char in pixels
CHAR_HEIGHT = 13 #height of a char in pixels

GRAY_SCALE = " .:!/r(l1Z4H9W8$@" #gradient in characters for graphics

#everything below is precalculated
PIXELS_PER_CHAR = CHAR_WIDTH * CHAR_HEIGHT
PIXEL_WIDTH = CHAR_WIDTH * WIDTH
PIXEL_HEIGHT = CHAR_HEIGHT * HEIGHT
NUMBER_OF_PIXELS = PIXEL_WIDTH * PIXEL_HEIGHT
NUMBER_OF_CHARS = WIDTH * HEIGHT