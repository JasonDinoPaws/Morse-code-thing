import RPi.GPIO as GPIO

BuzPin = [Pin]
Button = [Pin]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Buzzer = GPIO.WMB(BuzPin,100)
GPIO.setup(Button,GPIO.IN)


while True:
  if GPIO.input(Button) != 0: Buzzer.start(1)
  else: Buzzer.stop()
