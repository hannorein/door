import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # door input
GPIO.setup(17, GPIO.IN) # movement input
GPIO.setup(27, GPIO.IN) # sound input
GPIO.setup(22, GPIO.OUT) # RED out
GPIO.setup(23, GPIO.OUT) # moon out
GPIO.setup(24, GPIO.IN) # rfid in
GPIO.setup(12, GPIO.OUT) # buzzer
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) # button
buz = GPIO.PWM(12, 1000)
GPIO.output(22,1) 
GPIO.output(23,1) 

last_movement = 0
last_movement_for_moon = 0
last_sound = 0
ring_alarm = -1

def detect_sound(channel):
    global last_sound
    last_sound = time.time()
    with open("sound_lastminute.txt", "w") as f:
        f.write("1")
GPIO.add_event_detect(27, GPIO.BOTH, callback=detect_sound)

def detect_movement(channel):
    global last_movement
    global last_movement_for_moon
    last_movement = time.time()
    last_movement_for_moon = time.time()
    with open("movement_lastminute.txt", "w") as f:
        f.write("1")
GPIO.add_event_detect(17, GPIO.BOTH, callback=detect_movement)

def detect_door(channel):
    global ring_alarm 
    #print("dppr cjhamged", GPIO.input(4))
    with open("door_lastminute.txt", "w") as f:
        if GPIO.input(4)==0:
            # door opens
            if GPIO.input(24)==0 and GPIO.input(25)==1: # not unlocked
                if ring_alarm==-1: # no repeat
                    ring_alarm = 35
            f.write("1")
        else:
            # door closes
            ring_alarm = 0
            f.write("0")
GPIO.add_event_detect(4, GPIO.BOTH, callback=detect_door)


while True:
    if last_movement_for_moon!=0: 
        GPIO.output(23,0) # turn on moon 
        if time.time() - last_movement_for_moon > 2:
            GPIO.output(23,1) # turn off moon 
            last_movement_for_moon = 0
    if last_movement!=0 and time.time() - last_movement > 60:
        with open("movement_lastminute.txt", "w") as f:
            f.write("0")
        last_movement = 0
    if last_sound!=0 and time.time() - last_sound > 60:
        with open("sound_lastminute.txt", "w") as f:
            f.write("0")
        last_sound = 0

    if ring_alarm>-1:
        ring_alarm -=1
    if ring_alarm>=0:
        if ring_alarm%2==1:
            buz.start(50)
            GPIO.output(22,0) 
        else:
            buz.stop()
            GPIO.output(22,1) 
    time.sleep(0.1)
