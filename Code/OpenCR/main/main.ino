/*
  Project:      CAGIUS
  Description:  Main of the OpenCR.
  Authors:      Florence Millette
              Aissatou
              Alexandre
              Laurie Croteau
*/

// ========= Libraries ========
#include <Arduino.h>
#include <DynamixelWorkbench.h>
#include "serialcomm_functions.hpp"


// ========= Constant =========



// ========= Enumerations =====

enum State {
  Off, // attente du start de la cage
  Wait, // en attente de message de la camera
  Washing, // cycle de nettoyage
};

// ========= Variables ========

enum State current_state;
String msg;

// ========= Functions ========

void setup() {
  // put your setup code here, to run once:
  comm_init();
  current_state = Init;
}

void loop() {
  // put your main code here, to run repeatedly:
  switch (current_state) {
    case Off:
      // waiting for the start signal
      send_msg("En attente du lancement de la cage");
      msg = get_msg();
      if (should_start(msg) == true)
      {
        send_msg("Cage armee");
        current_state = Wait;
      }

      break;
    case Wait:
      // Waiting for the Camera or the stop of the cage signal
      msg = get_msg();
      if (should_stop(msg) == true)
      {
        send_msg("Cage arretee");
        current_state = Off;
      }

      // statement sur la camera

      break;
    case Washing:
    
      // nettoyage de la cage
      
      break;
  }

}
