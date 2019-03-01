import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)

# print relay on and send GPIO LOW six times with one second delay in between
# using six, one second pauses in case cron job for relayoff.sh is executed during a requested on
# relay activation will resume in case these two events meet 
# six second sleep would not resume GPIO LOW state if interrupted

print "Relay on"
GPIO.output(23,GPIO.LOW)
time.sleep(1)
GPIO.output(23,GPIO.LOW)
time.sleep(1)
GPIO.output(23,GPIO.LOW)
time.sleep(1)
GPIO.output(23,GPIO.LOW)
time.sleep(1)
GPIO.output(23,GPIO.LOW)
time.sleep(1)
GPIO.output(23,GPIO.LOW)
time.sleep(1)

# print relay off and return GPIO to HIGH
print "Relay off"
GPIO.output(23,GPIO.HIGH)
