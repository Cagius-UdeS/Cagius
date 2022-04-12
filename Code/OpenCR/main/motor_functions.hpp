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

#if defined(__OPENCM904__)
#define DEVICE_NAME "3" // Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#elif defined(__OPENCR__)
#define DEVICE_NAME ""
#endif

//----------motor--------------
const uint8_t MOTOR_TRAPPES_ID = 2; 
const uint8_t MOTOR_POUBELLE_ID = 1;
const uint8_t MOTOR_CONVOYEUR_ID = 3;
const uint8_t MOTOR_VIS_ID = 4;

//----------utilisateion--------------
const uint8_t DELTA_POS = 20;
const int32_t V_Trappes = 50;     // vitesse des trappes
const int32_t V_Convoyeur = 25;   // vitesse du convoyeur
const int32_t V_Poubelle = -100;    // vitesse rotation de la vis sans fin
const int TIME_PER_TROURS = 5000; // temps nécessaire pour effectuer un demi tour de convoyeur
const int32_t PI_SUR_2 = 1000;          // position de pi/2 rad
const unsigned long DELAY_PI_SUR_2 = 3000;  // temps nécessaire a faire PI/2 avec vitesse des trappes
const unsigned long DELAY_CONV_10Percent = 7000;  // temps nécessaire a faire 10 pourcentde l'allé du convoyeur
const unsigned long DELAY_POUBELLE_FREQCALCUL = 1000;  // delay calcul
const int32_t HOME_TRAPPES = 0;
const int32_t HOME_POUBELLE = 0;
const int32_t ELMT_TRAPPES = 2;
const int32_t ELMT_POUBELLE = 1;
const int INCREMENT_POUBELLE_MAX = 60;

const float PERCENT_MAX_CURRENT = 0.1;

// ========= Functions prototype ========

void init_motors(DynamixelWorkbench&  motor);

bool tourne_continu_NMBTours(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

int tourne_continu_Torque(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_torque, int percent);

bool tourne_continu_Torque_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours, int percent, int ii);

bool tourne_Xrad_ReturnPos(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad, uint8_t elmt);

bool tourne_Xrad_and_Stop(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad);

void stop_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs);

void readCurrent(DynamixelWorkbench&  motor, uint8_t motor_IDs);

void home_motor(DynamixelWorkbench&  motor, uint8_t motor_IDs);

#endif
