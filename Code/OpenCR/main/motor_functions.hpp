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

// ========= Functions prototype ========

void init_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs);

bool tourne_continu_NMBTours(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

bool tourne_continu_NMBTours_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

bool tourne_continu_Torque(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

bool tourne_continu_Torque_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours);

void stop_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs);

#endif
