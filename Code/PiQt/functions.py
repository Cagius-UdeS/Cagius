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

def init_comm(port, baudrate):
    """Initialize the communication with the wanted serial device.
    """
    print("Opening Serial communication with {0}.".format(port))
    ser = serial.Serial(port, baudrate)
    ser.flush()
    return ser


def print_received_data(data):
    print("Received : '{0}'\n".format(data))


def print_sent_data(data):
    print("Sent : '{0}'".format(data))


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
    message = "{0}{1}\n".format(ID_PI, data)
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


"""if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', required=True, help='Port used for serial communication.')
    parser.add_argument('-d', action='store_true', help='Run demo program.')
    args = parser.parse_args()
    port = args.p

    if args.d:
        print("Opening Serial communication with {0}.".format(port))
        with serial.Serial(port, baudrate) as ser:
            ser.flush()
            print_received_data(get_data(ser))

            print_sent_data(send_data(ser, "0START"))
            print_received_data(get_data(ser))

            #print_sent_data(send_data(ser, nut_to_string(0, 12, 34)))
            #print_received_data(get_data(ser))
            #print_sent_data(send_data(ser, nut_to_string(1, -56, -78)))
            #print_received_data(get_data(ser))
            print_sent_data(send_data(ser, "0WASH 50"))
            print_received_data(get_data(ser))


            print_sent_data(send_data(ser, "0END"))
            print_received_data(get_data(ser))

            print("Closing Serial communication with {1}.".format(port))"""