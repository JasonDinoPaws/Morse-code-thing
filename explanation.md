### Materals List
1 Rasberry pi,
1 BreadBoard,
1 Passive Buzzer,
1 Button Module,
6 M-F Wires,

--------------------------------------------------------
### Explanation
First you have to set up your Breadboard GPIO pings by

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Once you have set up your breadboard you need to set up your pins for the Buzzer and the Touch Module by
PWB allows you to set in frequenceys for stuff like the buzzer.
GPIO.IN Sets up the GPIO to check if it has recevied infomation from the touch module.

BuzPin = [Pin]
Button = [Pin]
Buzzer = GPIO.PMB(BuzPin,100)
GPIO.setup(Button,GPIO.IN)

And Finally to make this thing work by
GPIO.input([PIN]) Allows you you get a pin if it is set up as GPIO.IN to get a 1 if the Button Module is being Press down and 0 if it is not.

while True:
  if GPIO.input(Button) != 0: Buzzer.start(1)
  else: Buzzer.stop()

