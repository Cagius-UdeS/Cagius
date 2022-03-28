from functions          import *
import time
import argparse
import serial

def init_sequence():
    """Initialize the system.

    Read the arguments provided to the program.
    Initialize the camera.
    Initialize the communication.
    Start the main program on the OpenCR.
    """
    baudrate = 57600
    port = "/dev/ttyACM0"
    ser = init_comm(port, baudrate)
    init_opencr(ser)
    #off_state(ser)
    return port, ser



def init_comm(port, baudrate):
    """Initialize the communication with the wanted serial device.
    """
    print("Opening Serial communication with {0}.".format(port))
    ser = serial.Serial(port, baudrate)
    ser.flush()
    return ser


def init_opencr(ser):
    """Start the main program on the OpenCR.

    Verify if the OpenCR is currently sleeping
    """
    msg = get_data(ser)
    print_received_data(msg)
    # Confirm the OpenCR is waiting to start
    #if msg != "En attente du lancement de la cage":
     #   raise SerialError("The OpenCR is not waiting to start. Try restarting it.")



def off_state(ser):
    wait_for_data(ser, any)


def activate_state(ser):
    print_sent_data(send_data(ser, "START"))
    #print_received_data(get_data(ser))

    msg = get_data(ser)
    print_received_data(msg)

    """if msg == "En attente dinstruction":
        print_received_data(msg)
    else:
        send_data(ser, "START")"""


def clean_state(ser):
    print_sent_data(send_data(ser, "WASH 50 50"))
    print_received_data(get_data(ser))
    
    #msg = wait_for_data(ser, "Nettoyage fini")
    #off_state()
    

def trash_state(ser):
    print_sent_data(send_data(ser, "TRASH"))
    print_received_data(get_data(ser))



def stop_state(ser):
    """Stop all systems.

    Stop the main program on the OpenCR.
    Release the camera.
    Close the communication with the serial device.
    """
    print_sent_data(send_data(ser, "END"))
    print_received_data(get_data(ser))

    #print("Closing Serial communication with {0}.".format(port))
    #ser.close()