import urandom
import oled
import buttons
import utime
import buzzer


def says():
    while True:
        try:
            simon_list = []
            print("starting simon from the top")
                   # adds number to list
            for i in range(5):   #rund through list inverting the selected oled in list for 1 second
                r = urandom.randint(0,3)
                simon_list.append(r)
                oled.simonShow(simon_list)
                utime.sleep_ms(100)
                for i in simon_list:
                    while True:
                        utime.sleep_ms(10)
                        but = buttons.getOnly()
                        if not but:
                            continue
    
                        if but[0] != i:
                            buzzer.stop()
                            buzzer.wrongAnswer()
                            print("incorrect sequence")
                            buzzer.start()
                            utime.sleep_ms(100)
                            raise
                    
                        print("correct sequence")
                        utime.sleep_ms(250)

                        break

                buzzer.stop()
                buzzer.rightAnswer()
                buzzer.start()
                utime.sleep_ms(50)

        except Exception as e:
            print(e)
            continue

        break