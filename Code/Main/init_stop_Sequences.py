import sys

sys.path.insert(0, '/home/pi/Documents/Cagius/Code/PiCamera/Object_Detection_Files')
import FonctionsCam as funCam
from functions_Comm          import *

import time
import argparse
import serial

qteP = 0

def init_sequence():
    """Initialize the system.

    Initialize the communication.
    Initialize the OpenCR.
    Initialize the camera.
    """

    baudrate = 57600
    port = "/dev/ttyACM0"
    ser = init_comm(port, baudrate)
    init_opencr(ser)
    init_camera()

    return port, ser


def init_comm(port, baudrate):
    """Initialize the communication with the wanted serial device.
    """

    print("Opening Serial communication with {0}.".format(port))
    ser = serial.Serial(port, baudrate)
    ser.flush()
    return ser


def init_opencr(ser):
    """Initialize the OpenCR

    Send initilization commands
    Wait for message for confirmation
    """

    print("Initialization the OpenCR\n")
    print_sent_data(send_data(ser, "INIT"))
    msg = wait_for_data(ser, "En attente du lancement de la cage")
    
    # Confirm the OpenCR is waiting to start
    if msg != "En attente du lancement de la cage":
       raise SerialError("The OpenCR is not waiting to start. Try restarting it.")


def init_camera():
    """Initialize the camera

    Call function to initialize GPIOs
    """

    print("Initialization the camera\n")
    funCam.InitGPIO()


def activate_state(ser):
    """Activate the cage

    Send starting commands to the OpenCR.
    Wait for messages for confirmation
    Return True to activate the thread
    """

    print_sent_data(send_data(ser, "START"))
    # Confirm the cage is ready to start 
    msg1 = wait_for_data(ser, "Cage armee")
    # Confirm the cage is waiting for instructions
    msg2 = wait_for_data(ser, "En attente dinstruction")

    return True                         



def clean_state(ser):
    """Clean the cage

    Send cleaning commands to the OpenCR.
    Wait for messages for confirmation
    Return boolean to verify to washing process is over and percentage of trash used
    """

    V,N = funCam.Scan()
    global qteP
    qteP = qteP + (V/3)                            # Quantit?? en fractions de l'usure de la liti??re
    PP = round(qteP/3 * 100, None)                 # Pourcentage poubelle

    if (N == 0):
        message = "WASH " + str(V) + " " + str(PP)
        print_sent_data(send_data(ser, message))
        # Confirm the cleaning process started
        msg1 = wait_for_data(ser, "Nettoyage en cours")
        # Confirm the cleaning process is over
        msg2 = wait_for_data(ser, "Nettoyage fini")
        # Confirm the cage is waiting for instructions
        msg3 = wait_for_data(ser, "En attente dinstruction")
        return True, V
    else:
        return False, V
    

def trash_state(ser):
    """Empty the cage trash

    Send trashing commands to the OpenCR.
    Wait for messages for confirmation
    """

    print_sent_data(send_data(ser, "TRASH"))
    # Confirm the emptying process started
    msg1 = wait_for_data(ser, "Nettoyage de la poubelle amorce")
    # Confirm the cage trash is empty
    msg2 = wait_for_data(ser, "Nettoyage de la poubelle fini")
    # Confirm the cage is waiting for instructions
    msg3 = wait_for_data(ser, "En attente dinstruction")



def stop_state(ser):
    """Stop the cage

    Send stopping commands to the OpenCR
    Wait for message for confirmation
    """

    print_sent_data(send_data(ser, "END"))
    # Confirm the cage was stopped
    msg = wait_for_data(ser, "Cage arretee")
