import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pin=26
GPIO.setup(led_pin, GPIO.OUT)

try:
  GPIO.output(led_pin, GPIO.LOW)

except KeyboardInterrupt:
    pass
GPIO.cleanup()
