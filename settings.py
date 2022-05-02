import buttons
import oled 
import utime

military = False
alarm = None

class change():

    def m():
        global military
        if military is False:
            count = 1
        else:
            count = 0
        if military == False:
            oled.writeDigit(1, 0)
            oled.writeDigit(2, 1)
            oled.writeDigit(0, 2)
            oled.writeDigit(0, 3)
        else:
            oled.writeDigit(2, 0)
            oled.writeDigit(4, 1)
            oled.writeDigit(0, 2)
            oled.writeDigit(0, 3)
        utime.sleep_ms(500)
        while True:

            try:
                if buttons.getOnly()[0] == 1:
                    count += 1
                    if count % 2 != 0:
                        military = False
                        oled.writeDigit(1, 0)
                        oled.writeDigit(2, 1)
                        oled.writeDigit(0, 2)
                        oled.writeDigit(0, 3)
                    else:
                        oled.writeDigit(2, 0)
                        oled.writeDigit(4, 1)
                        oled.writeDigit(0, 2)
                        oled.writeDigit(0, 3)
                        military = True
                    utime.sleep_ms(100)          

                else:
                    try:
                        try:
                            countInvert = 0
                            while buttons.get()[0] == 0:
                                
                                if countInvert == 0:
                                    oled.invert(0)
                                countInvert += 1
                                try:
                                    if buttons.get()[1] == 1:
                                        oled.invert(0)
                                        raise
                                except IndexError:
                                    continue
                        except IndexError:
                            print("0 not pressed")
                        if countInvert != 0:
                            oled.invert(0)
                    except IndexError:
                        continue

            except IndexError:
                continue
            except Exception as e:
                print(e)
                return

    def a():
        global alarm
        hourTen = 0
        hourOne = 0
        minuteTen = 0
        minuteOne = 0

        oled.writeDigit(0, 0)
        oled.writeDigit(0, 1)
        oled.writeDigit(0, 2)
        oled.writeDigit(0, 3)
        utime.sleep_ms(1000)
        lock = False
        while True:
            try:
                if buttons.getOnly()[0] == 0:
                    
                    utime.sleep_ms(500)
                    count = 0
                    try:
                        while buttons.get()[0] == 0:
                            try:
                                if count == 0:
                                    oled.invert(0)
                                count += 1
                                if buttons.get()[1] == 2:
                                    oled.invert(0)
                                    raise
                            except IndexError:
                                continue
                    except IndexError:
                        print("only 0 pressed")
                    
                    if count != 0:
                        oled.invert(0)
                    
    
                    if hourTen == 2:
                        hourTen = 0
                        oled.writeDigit(hourTen, 0)
                        lock = False
                        utime.sleep_ms(250)
                    else:
                        hourTen += 1
                        oled.writeDigit(hourTen, 0)
                        if hourTen == 1:
                            lock = False
                        else:
                            lock = True
                        utime.sleep_ms(250)

                elif buttons.getOnly()[0] == 1:
                    if lock:
                        if hourOne >= 4:
                            hourOne = 0
                            oled.writeDigit(hourOne, 1)
                            utime.sleep_ms(250)
                        else:
                            hourOne += 1
                            oled.writeDigit(hourOne, 1)
                            utime.sleep_ms(250)
                    else:
                        if hourOne == 9:
                            hourOne = 0
                            oled.writeDigit(hourOne, 1)
                            utime.sleep_ms(250)
                        else:
                            hourOne += 1
                            oled.writeDigit(hourOne, 1)
                            utime.sleep_ms(250)
                elif buttons.getOnly()[0] == 2:
                    if minuteTen == 5:
                        minuteTen = 0
                        oled.writeDigit(minuteTen, 2)
                        utime.sleep_ms(250)
                    else:
                        minuteTen += 1
                        oled.writeDigit(minuteTen, 2)
                        utime.sleep_ms(250)
                elif buttons.getOnly()[0] == 3:
                    if minuteOne == 9:
                        minuteOne = 0
                        oled.writeDigit(minuteOne, 3)
                        utime.sleep_ms(250)
                    else:
                        minuteOne += 1
                        oled.writeDigit(minuteOne, 3)
                        utime.sleep_ms(250)

            except IndexError:
                continue
            except Exception as e:
                print(e)
                break  
        alarm = []
        alarm.append(str(hourTen))
        alarm.append(str(hourOne))
        alarm.append(str(minuteTen))
        alarm.append(str(minuteOne))
        for i in range(len(alarm)):
            if int(alarm[i]) != 0:
                break
            elif i == 3:
                alarm = None
        return

    def t():
        hourTen = 0
        hourOne = 0
        minuteTen = 0
        minuteOne = 0

        oled.writeDigit(0, 0)
        oled.writeDigit(0, 1)
        oled.writeDigit(0, 2)
        oled.writeDigit(0, 3)
        utime.sleep_ms(1000)
        lock = False
        while True:
            try:
                if buttons.getOnly()[0] == 0:
                    
                    utime.sleep_ms(500)
                    count = 0
                    try:
                        while buttons.get()[0] == 0:
                            try:
                                if count == 0:
                                    oled.invert(0)
                                count += 1
                                if buttons.get()[1] == 3:
                                    oled.invert(0)
                                    raise
                            except IndexError:
                                continue
                    except IndexError:
                        print("only 0 pressed")
                    
                    if count != 0:
                        oled.invert(0)
                    
    
                    if hourTen == 2:
                        hourTen = 0
                        oled.writeDigit(hourTen, 0)
                        lock = False
                        utime.sleep_ms(250)
                    else:
                        hourTen += 1
                        oled.writeDigit(hourTen, 0)
                        if hourTen == 1:
                            lock = False
                        else:
                            lock = True
                        utime.sleep_ms(250)

                elif buttons.getOnly()[0] == 1:
                    if lock:
                        if hourOne >= 4:
                            hourOne = 0
                            oled.writeDigit(hourOne, 1)
                            utime.sleep_ms(250)
                        else:
                            hourOne += 1
                            oled.writeDigit(hourOne, 1)
                            utime.sleep_ms(250)
                    else:
                        if hourOne == 9:
                            hourOne = 0
                            oled.writeDigit(hourOne, 1)
                            utime.sleep_ms(250)
                        else:
                            hourOne += 1
                            oled.writeDigit(hourOne, 1)
                            utime.sleep_ms(250)
                elif buttons.getOnly()[0] == 2:
                    if minuteTen == 5:
                        minuteTen = 0
                        oled.writeDigit(minuteTen, 2)
                        utime.sleep_ms(250)
                    else:
                        minuteTen += 1
                        oled.writeDigit(minuteTen, 2)
                        utime.sleep_ms(250)
                elif buttons.getOnly()[0] == 3:
                    if minuteOne == 9:
                        minuteOne = 0
                        oled.writeDigit(minuteOne, 3)
                        utime.sleep_ms(250)
                    else:
                        minuteOne += 1
                        oled.writeDigit(minuteOne, 3)
                        utime.sleep_ms(250)

            except IndexError:
                continue
            except Exception as e:
                print(e)
                break  
        time = []
        time.append(str(hourTen))
        time.append(str(hourOne))
        time.append(str(minuteTen))
        time.append(str(minuteOne))
        for i in time:
            if i != 0:
                break
            time = None
        return time
