from machine import I2C, Pin
from urtc import DS3231
from ssd1306 import SSD1306_I2C
import utime
import oled

# i2c_rtc = I2C(1,scl = Pin(7),sda = Pin(6),freq = 100000)
rtc = DS3231(oled.i2c1, address=0x68)
utime.sleep_ms(100)


def updateTime():
    year = int(input("Year : "))
    month = int(input("month (Jan --> 1 , Dec --> 12): "))
    date = int(input("date : "))
    day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
    hour = int(input("hour (24 Hour format): "))
    minute = int(input("minute : "))
    second = int(input("second : "))
    now = (year,month,date,day,hour,minute,second,0)
    rtc.datetime(now)

def getTime():
    list = []
    hour = "{:02d}".format(rtc.datetime().hour)
    minute = "{:02d}".format(rtc.datetime().minute)
    for i in str(hour):
        list.append(int(i))
    for i in str(minute):
        list.append(int(i))
    return list

t = getTime()
print(t)
for i in range(len(t)):
    oled.writeDigit(t[i], i)