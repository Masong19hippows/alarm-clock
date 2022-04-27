from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import digits

i2c0 = I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
i2c1 = I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)
oled0 = SSD1306_I2C(128, 64, i2c0)
oled1 = SSD1306_I2C(128, 64, i2c1)
oled2 = 
oled3 = 

oleds = [oled0, oled1]
scale = 6


def writeDigit(number, oled):
    for y, row in enumerate(digits.digit(number)):
        for x, c in enumerate(row):
            oleds[oled].pixel(x*scale + 38, y*scale + 4 , c)
    oleds[oled].show()

def invert(oled):
    oleds[oled].invert(1)

writeDigit(number = 6, oled = 1)
writeDigit(number = 6, oled = 0)