import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pin1=13
GPIO.setup(led_pin1, GPIO.OUT)

try:
  GPIO.output(led_pin1, GPIO.HIGH)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
