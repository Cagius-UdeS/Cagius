/*
  Project:      CAGIUS
  Description:  Header: Function Motor
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
                Natael Laroche-Latulippe
*/

#ifndef motor_functions_h
#define motor_functions_h

#include <Arduino.h>
#include <stdint.h>
#include <DynamixelWorkbench.h>
#include <vector>

// ========= Constant =========

//----------motor--------------
const uint8_t MOTOR_TRAPPES_ID = 2; 
const uint8_t MOTOR_POUBELLE_ID = 1;
const uint8_t MOTOR_CONVOYEUR_ID = 4;
const uint8_t MOTOR_VIS_ID = 3;

//----------utilisateion--------------
const uint8_t DELTA_POS = 20;
const int32_t V_Trappes = 50;     // vitesse des trappes
const int32_t V_Convoyeur = 25;   // vitesse du convoyeur
const int TIME_PER_TROURS = 6000; // temps nécessaire pour effectuer un tour de convoyeur
const int32_t PI_SUR_2 = 1023;          // position de pi/2 rad
const unsigned long DELAY_PI_SUR_2 = 3000;  // temps nécessaire a faire PI/2 avec vitesse des trappes
const int32_t HOME = 0;

// ========= Functions prototype ========

void init_motors(DynamixelWorkbench&  motor);

bool tourne_continu_NMBTours(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

bool tourne_continu_Torque(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_torque);

bool tourne_continu_Torque_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

bool tourne_Xrad_ReturnPos(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad);

bool tourne_Xrad_and_Stop(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad);

void stop_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs);

#endif
