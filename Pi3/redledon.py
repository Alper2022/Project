import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin=26

GPIO.setup(led_pin, GPIO.OUT)

try:
  GPIO.output(led_pin, GPIO.HIGH)

except KeyboardInterrupt:
    pass

