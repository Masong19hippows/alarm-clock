import oled
import buttons
import buzzer
import clock
import oled
import settings
import utime
import alarm
import simon

time = clock.getTime()
for i in range(len(time)):
    oled.writeDigit(number = time[i], oled = i)

try:

    while True:

        utime.sleep_ms(1000)
        try:
            while True:
                newTime = clock.getTime()
                print("time is ", newTime)
                for i in range(len(newTime)):
                    if time[i] != newTime[i]:
                        oled.writeDigit(number = newTime[i], oled = i)
                time = newTime

                t = clock.getTime(True)
                print("alarm checks are", t, "and", settings.alarm)
                if alarm.check(t):
                    settings.alarm = None
                    print("alarm check triggered")
                    for i in range(len(t)):
                        oled.writeDigit(number = t[i], oled = i)
                    print("exception")
                    utime.sleep_ms(1000)
                    raise

                try:
                    count = 0
                    while buttons.get()[0] == 0:
                        if count == 0:
                            oled.invert(0)
                        count += 1
                        utime.sleep_ms(25)

                        try:
                            if buttons.get()[1] == 3:
                                count = 0
                                oled.invert(0)
                                print("changing time")
                                clock.updateTime(settings.change.t())
                                print("done changing time")
                                time = clock.getTime()
                                for i in range(len(time)):
                                    oled.writeDigit(number = time[i], oled = i)
                                break

                            elif buttons.get()[1] == 2:
                                count = 0
                                oled.invert(0)   
                                print("changing alarm")
                                settings.change.a()
                                print("done changing alarm")
                                time = clock.getTime()
                                for i in range(len(time)):
                                    oled.writeDigit(number = time[i], oled = i)
                                break          
                            elif buttons.get()[1] ==  1:
                                count = 0
                                oled.invert(0)
                                print("changing military")
                                settings.change.m()
                                print("done changing military")
                                time = clock.getTime()
                                for i in range(len(time)):
                                    oled.writeDigit(number = time[i], oled = i)
                                break

                        except IndexError:
                            continue
                    
                except IndexError:
                    if count != 0:
                        oled.invert(0)
                    
                    print("no buttons pressed")
                utime.sleep_ms(2500)
        except Exception as e:
            print(e)

            buzzer.start()
            for i in range(4):
                oled.invert(i)

            while True:
                if buttons.get():
                    break
                else:
                    utime.sleep_ms(50)
                    continue
            for i in range(4):
                oled.invert(i)
            try:
                simon.says()
            except Exception as e:
                print(e)
            buzzer.stop()
            utime.sleep(1)
            print("Simon Says completed")
            continue
    
except KeyboardInterrupt:
    print(e)
    buzzer.st
    utime.sleep(5)