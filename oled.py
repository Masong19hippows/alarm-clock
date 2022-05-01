from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import digits
import utime


i2c1 = I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled1 = SSD1306_I2C(128, 64, i2c1)
i2c0 = I2C(1 ,sda=Pin(2), scl=Pin(3), freq=400000)
oled0 = SSD1306_I2C(128, 64, i2c0)


scale = 6

def oleds(num):
      
    if num == 0:
        return oled0
    elif num == 1:
        return oled0
    elif num == 2:
        return oled1
    elif num == 3:
        return oled1
    else:
        raise


def writeDigit(number, oled):
    display = oleds(oled)
    pos = 0
    if oled == 1 or oled == 3:
        pos = 74
    count = 0
    for y, row in enumerate(digits.digit(number)):
        for x, c in enumerate(row):
            display.pixel(x*scale + pos, y*scale + 4 , c)
    display.show()

def invert(oled):
    display = oleds(oled)
    pos = 0
    if oled == 1 or oled == 3:
        pos = 64
    for y in range(64):
        for x in range(64):
            c = display.pixel(x + pos, y)
            if c == 0:
                display.pixel(x + pos, y, 1)
            elif c == 1:
                display.pixel(x + pos, y, 0)
    display.show()

def simonShow(list):
    for i in list:
        invert(i)
        utime.sleep_ms(1000)
        invert(i)