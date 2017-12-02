from firebase import firebase
firebase = firebase.FirebaseApplication('https://viz-pass.firebaseio.com/', None)
isReady = firebase.get('/status/inReady',None)
print isReady
import RPi.GPIO as GPIO
import time
while True:
    if (firebase.get('/status/inRange',None) == False):
        GPIO.setmode(GPIO.BCM)

        TRIG = 23
        ECHO = 24

        print "Distance Measurement In Progress"

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup (ECHO, GPIO.IN)

        GPIO.output(TRIG,False)
        print "Waiting for Sensor To Settle"
        time.sleep(2)

        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        
        if (distance < 50):
            firebase.put('status','inRange',True)

        #print "Distance:", distance, "cm"

        GPIO.cleanup()