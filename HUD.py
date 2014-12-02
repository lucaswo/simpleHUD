import time
import signal
import sys

from Adafruit_LED_Backpack import AlphaNum4

#initialise display
display = AlphaNum4.AlphaNum4()
#bit mask mapping for mirrored numbers
numbers = {
    '0': 0x003F,
    '1': 0x0006,
    '2': 0x00ED,
    '3': 0x008F,
    '4': 0x00D6,
    '5': 0x00DB,
    '6': 0x00FB,
    '7': 0x000E,
    '8': 0x00FF,
    '9': 0x00DF
}

display.begin()

print 'Press Ctrl-C to quit.'

def reset_display():
    display.clear()
    display.write_display()

#show mirrored version of the number by using the mirrored bit mask and shifting everything to the right
def show_mirrored_digit(digit):
    digit_length = len(digit)
    if digit_length > 4:
        return

    display.clear()

    for i, d in enumerate(digit):
        display.set_digit_raw(i+(4-digit_length), numbers[d])

    display.write_display()

#clear display on exit
def signal_handler(signal, frame):
    reset_display()
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

display.clear()

for x in [1337]:
    show_mirrored_digit(str(x))
    time.sleep(0.1)

while True:
    time.sleep(1)
