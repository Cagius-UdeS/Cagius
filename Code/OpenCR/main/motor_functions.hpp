/*
  Project:      CAGIUS
  Description:  Header: Function Motor
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
*/

#ifndef motor_functions_h
#define motor_functions_h
#include <stdint.h>
#include <DynamixelWorkbench.h>

class DynamixelWorkbench;

const uint8_t MOTOR_TRAPPES_ID = 1;
const uint8_t MOTOR_POUBELLE_ID = 2;
const uint8_t MOTOR_CONVOYEUR_ID = 3;
const uint8_t MOTOR_VIS_ID = 4;
const uint8_t DELTA_POS = 20;
const float DELTA_RAD = 0.01;

// ========= Functions prototype ========

void init_motors(DynamixelWorkbench&  motor);

bool tourne_continu_NMBTours(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

bool tourne_continu_NMBTours_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

bool tourne_continu_Torque(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

bool tourne_continu_Torque_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

float tourne_Xrad(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad);

bool tourne_Xrad_ReturnPos(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad);

void stop_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs);

#endif
