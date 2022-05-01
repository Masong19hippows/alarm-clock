import settings
import clock

def check(time):
    if settings.alarm == None:
        return False
    else:
        for i in range(len(settings.alarm)):
            if int(settings.alarm[i]) != int(time[i]):
                return False

        return True