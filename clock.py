from machine import I2C, Pin
from urtc import DS3231
import utime
import oled
import settings
import _thread

rtc = DS3231(oled.i2c1, address=0x68)
utime.sleep_ms(100)


def updateTime(list):
    if list is None:
        return
    now = (2022,4,29,5,int(str(list[0]) + str(list[1])),int(str(list[2]) + str(list[3])),0,0)
    print("updating time with", now)
    rtc.datetime(now)

def getTime(alarm = False):

    list = []
    hour = rtc.datetime().hour

    if alarm == False:
        if settings.military == False:
            if hour == 0:
                hour = 12
            elif hour == 12:
                hour = 12
            elif hour > 12:
                hour %= 12

    hour = "{:02d}".format(hour)
    minute = "{:02d}".format(rtc.datetime().minute)

    for i in str(hour):
        list.append(int(i))
    for i in str(minute):
        list.append(int(i))
    return list