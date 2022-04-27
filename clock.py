from machine import I2C, Pin
from urtc import DS3231
from ssd1306 import SSD1306_I2C
import utime

i2c_rtc = I2C(1,scl = Pin(7),sda = Pin(6),freq = 100000)
rtc = DS3231(i2c_rtc, address=0x68)
utime.sleep_ms(100)


def updateTime():

    hour = rtc.datetime().hour
    minute = rtc.datetime().minute
    return [hour, minute]

def getTime():


    return rtc.datetime()

for i in updateTime():
    print(i)