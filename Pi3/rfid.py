import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)

reader=SimpleMFRC522()

def turnon():
    GPIO.cleanup()
    with open ('redledon.py','r') as f:
       on= f.read()
    exec(on)
try:
   turnon()
   print('Please scan card!')
   id, text= reader.read()
   print (id)
   print (text) 
   with open('tagnum.txt', 'r') as f:
     text= f.read()
   if str(id) in text:
      with open('servo.py', 'r') as f:
         servo= f.read()
      with open('redledoff.py', 'r') as f:
          off= f.read() 
      GPIO.cleanup()
      exec(off)
      exec(servo)
   else:
      GPIO.cleanup()

except KeyboardInterrupt:
  pass

