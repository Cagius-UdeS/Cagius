import serial
import argparse
import time

encoding = "utf-8"
baudrate = 57600

ID_PI = '0'
ID_OPENCR = '1'

class SerialError(Exception):
    """ Raised when an error occurs with the OpenCR. """
    pass


def print_received_data(data):
    print("Received : '{0}'\n".format(data))


def print_sent_data(data):
    print("Sent : '{0}'\n".format(data))


def get_data(ser):
    """Read data from ser (a serial port).

    Ignore the message if it was sent by this device.
    Return the received data.
    """
    tmp = ser.readline().decode().rstrip()
    data = ""
    # The first char is the ID of the sender: if the ID is this
    # device's ID, ignore the message
    if tmp != "":
        if tmp[0] == ID_OPENCR:
            data = tmp[1:]
    return data


def send_data(ser, data):
    """Write data to ser (a serial port).

    Prepend the ID of the sender to the message.
    Return the sent message.
    """
    message = "{0}{1}".format(ID_PI, data)
    ser.write(message.encode())
    return message

def wait_for_data(ser, wanted):
    """Wait in this function until a wanted string is read.
    """
    data = get_data(ser)
    while data != wanted:
        data = get_data(ser)
        time.sleep(0.01)

    print_received_data(data)
    return data