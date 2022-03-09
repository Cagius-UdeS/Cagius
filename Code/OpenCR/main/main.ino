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
#include <stdint.h>
#include <DynamixelWorkbench.h>
#include <vector>
#include "serialcomm_functions.hpp"
#include "motor_functions.hpp"

// ========= Constant =========

//----------motor--------------

#if defined(__OPENCM904__)
  #define DEVICE_NAME "3" //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#elif defined(__OPENCR__)
  #define DEVICE_NAME ""
#endif  


// ========= Enumerations =====

enum State {
  Off, // attente du start de la cage
  Wait, // en attente de message de la camera
  Washing, // cycle de nettoyage
};

// ========= Constant =========

//uint8_t get_id[16];
//uint8_t scan_cnt = 0;
//uint8_t ping_cnt = 0;
const uint8_t MOTOR1_ID = 1;
const uint8_t MOTOR2_ID = 2;
const uint8_t MOTOR3_ID = 3;
const uint8_t MOTOR4_ID = 4;
const uint8_t DELTA_POS = 20;

// ========= Variables ========

enum State current_state;
String msg;

// ========= Variables =========

DynamixelWorkbench dyna;

// ========= Functions ========

void setup() {
  // put your setup code here, to run once:
  comm_init();
  current_state = Off;
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
      if (should_end(msg) == true)
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
