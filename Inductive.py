import time
import RPi.GPIO as GPIO

# Pin of Input
GPIOpin = -1

# Initial the input pin
def initialInductive(pin):
  global GPIOpin 
  GPIOpin = pin
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(GPIOpin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  print("Finished Initiation")
  print(GPIOpin)

# Detect Metal
def detectMetal():
  if(GPIOpin != -1):
    state = GPIO.input(GPIOpin)
    if state:
      print("Metal Detected")
    else :
      print("Metal Not Detected")
  else:
    print("Please Initial Input Ports")

# test module
if __name__ == '__main__':
  pin = 17
  initialInductive(pin)
  while True:
    detectMetal()
    time.sleep(0.2)
