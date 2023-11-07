import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader= SimpleMFRC522()

try:
   print('place rfid tag')
   text= input('enter something to write: ')
   print('now place tag to write')
   id,tek=reader.read()
   reader.write(text)
   with open ('tagnum.txt', 'a') as file:
     file.write(f'{str(id)} {text}\n')
   print('its done!')

finally:
  GPIO.cleanup()
