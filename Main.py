import RPi.GPIO as GPIO

BuzPin = [Pin]
Button = [Pin]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Buzzer = GPIO.WMB(BuzPin,100)
GPIO.setup(Button,GPIO.IN)

Buzzer.start(0)
Cycle = 0

while True:
  if GPIO.input(Button) != 0: Cycle = 1
  else: Cycle = 0

Buzzer.ChangeDudyCycle(Cycle)
    
