import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin=18

led_pin= 13

freq=50

GPIO.setup(pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

pwm= GPIO.PWM(pin, freq)

pwm.start(0)

try:
   GPIO.output(led_pin, GPIO.HIGH)
   graden= 180
   hoek= (graden / 18 ) + 2
   pwm.ChangeDutyCycle(hoek)
   time.sleep(10)

   GPIO.output(led_pin, GPIO.LOW)
   graden = 0
   hoek= (graden / 18 ) + 2 
   pwm.ChangeDutyCycle(hoek)
   time.sleep(2)

except KeyboardInterrupt:
  pass

pwm.stop()
GPIO.cleanup()
