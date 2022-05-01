import machine
import utime
import buzzer

button0 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
button1 = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
button3 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)


def get():
    buttonsPressed = []
    if not button0.value():
        buttonsPressed.append(0)
    if not button1.value():
        buttonsPressed.append(1)
    if not button2.value():
        buttonsPressed.append(2)
    if not button3.value():
        buttonsPressed.append(3)

    return buttonsPressed

def getOnly():

    buttonsPressed = []
    count = 0

    if not button0.value():
        buttonsPressed.append(0)
        count += 1
    if not button1.value():
        buttonsPressed.append(1)
        count += 1
    if not button2.value():
        buttonsPressed.append(2)
        count += 1
    if not button3.value():
        buttonsPressed.append(3)
        count += 1
    if count > 1:
        return []
    return buttonsPressed