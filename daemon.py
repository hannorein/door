import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # door input
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # movement input
GPIO.setup(27, GPIO.IN) # sound input
GPIO.setup(22, GPIO.OUT) # RED out
GPIO.setup(23, GPIO.OUT) # moon out
GPIO.setup(10, GPIO.OUT) # lock led out
GPIO.setup(24, GPIO.IN) # rfid in
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # button
GPIO.setup(12, GPIO.OUT) # buzzer
GPIO.setup(18, GPIO.OUT) # extreme buzzer 
buz = GPIO.PWM(12, 1000)
GPIO.output(22,1) 
GPIO.output(23,1) 

silent = False
ring_alarm = -1
lockled_flasher = 0

def increment_counter(filename):
    try:
        with open(filename, 'r' ) as fle:
            counter = int( fle.readline() ) + 1
    except:
        counter = 0
    with open(filename, 'w' ) as fle:
        fle.write( str(counter) )


def detect_sound(channel):
    increment_counter("sound_counter.txt")
GPIO.add_event_detect(27, GPIO.BOTH, callback=detect_sound)

def detect_movement(channel):
    increment_counter("movement_counter.txt")
GPIO.add_event_detect(17, GPIO.BOTH, callback=detect_movement)

def detect_button(channel):
    global ring_alarm 
    ring_alarm = -1
GPIO.add_event_detect(7, GPIO.BOTH, callback=detect_button)


def detect_door(channel):
    global ring_alarm 
    #print("dppr cjhamged", GPIO.input(4))
    if GPIO.input(4)==1:
        # door closes
        ring_alarm = -1
        return
    if ring_alarm > -1:
        # alarm currently underway
        return 
    if GPIO.input(4)==0: # door open
        increment_counter("door_counter.txt")
        time.sleep(0.2)
        if GPIO.input(4)==0: # door still open (not a fluke)
            if ring_alarm==-1: # no repeat
                ring_alarm = 90
                increment_counter("alarm_counter.txt")
GPIO.add_event_detect(4, GPIO.BOTH, callback=detect_door)

while True:
    #if GPIO.input(17): 
    #    GPIO.output(23,0) # turn on moon 
    #else:
    #    GPIO.output(23,1) # turn off moon 
    if ring_alarm>-1:
        ring_alarm -=1
    if ring_alarm>=0:
        if ring_alarm>=50 and ring_alarm%6!=0:
            #sparse alarm initially
            pass
        else:
            if silent:
                time.sleep(0.25)
            else:
                buz.start(50)
                GPIO.output(22,0) 
                if ring_alarm<25:
                    GPIO.output(18,1)
                time.sleep(0.25)
                GPIO.output(18,0) # always turn off extreme buzzer as precaution
                buz.stop()
                GPIO.output(22,1) 


        #if ring_alarm%2==1:
        #    buz.start(50)
        #    GPIO.output(22,0) 
        #else:
        #    buz.stop()
        #    GPIO.output(22,1) 
    GPIO.output(18,0) # always turn off extreme buzzer as precaution
    if silent==True:
        GPIO.output(10,0)
    else:
        lockled_flasher = not lockled_flasher
        if lockled_flasher:
            GPIO.output(10,1) 
        else:
            GPIO.output(10,0) 

    time.sleep(0.1)
    if GPIO.input(24)==1: # rfid unlocked 
        if silent==True:
            time.sleep(0.4)
            if GPIO.input(24)==1: # still rfid unlocked (not a fluke)
                time.sleep(1.0)
                silent = False
        else:    
            time.sleep(0.4)
            if GPIO.input(24)==1: # still rfid unlocked (not a fluke)
                time.sleep(1.0)
                silent = True
