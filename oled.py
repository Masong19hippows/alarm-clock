from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import digits

i2c = I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
scale = 6

def writeDigit(number):
    for y, row in enumerate(digits.digit(number)):
        for x, c in enumerate(row):
            oled.pixel(x*scale + 38, y*scale + 4 , c)
    oled.show()


def fillOled():

    oled.fill(1)  # Fill the entire oled with 1="on"
    oled.show()

def invert():
    oled.invert(1)
