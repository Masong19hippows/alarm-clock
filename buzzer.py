import machine
import utime
import _thread

global buzzCheck
buzzCheck = False

pin = machine.Pin(16, machine.Pin.OUT)

def buzz(oscilate = 500):
    global buzzer, buzzCheck
    buzzer = True
    while buzzer:
        buzzCheck = True
        try:
            pin(True)
            utime.sleep_ms(oscilate)
            pin(False)
            utime.sleep_ms(oscilate)
        except:
            pin(False)
            break
    buzzCheck = False

def start():
    _thread.start_new_thread(buzz, ())
    utime.sleep_ms(100)


def stop():
    global buzzer, buzzCheck
    buzzer = False
    while buzzCheck:
        continue
    utime.sleep_ms(100)



def buzzOscilate(amount, oscilate):
    amount = int( 2 * oscilate * amount)

    _thread.start_new_thread(buzz, (oscilate, ))
    utime.sleep_ms(amount)
    stop()


def wrongAnswer():
    buzzOscilate(amount = 4, oscilate = 50)


def rightAnswer():
    buzzOscilate(amount = 2, oscilate = 125)