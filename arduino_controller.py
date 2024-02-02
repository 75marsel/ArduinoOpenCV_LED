from pyfirmata import Arduino

PORT = 'COM3'

board = Arduino(PORT)

led_1 = board.get_pin('d:13:o')

def detection(status):
    if status == True:
        led_1.write(1)
    else:
        led_1.write(0)