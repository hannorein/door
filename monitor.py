import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #door
GPIO.setup(17, GPIO.IN) # movement input
GPIO.setup(27, GPIO.IN) # sound input
GPIO.setup(24, GPIO.IN) # rfid in
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) # button

last_door = 0
last_movement = 0

while True:
    print("door, movement, sound, rfid, button")
    print GPIO.input(4), GPIO.input(17), GPIO.input(27), GPIO.input(24), GPIO.input(25)

    time.sleep(0.1)
