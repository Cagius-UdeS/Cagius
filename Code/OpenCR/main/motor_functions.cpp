/*
  Project:      CAGIUS
  Description:  Function Motor
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
*/

#include "motor_functions.hpp"
#include <Arduino.h>

// ========= Functions ========

void init_motors(DynamixelWorkbench& motor, uint8_t motor_IDs)
{
        const char* motor_name = 1+"";
        uint16_t model_number = 0;
        const char* error_message;
        motor.init(motor_name, 57600, &error_message);
        motor.ping(motor_IDs, &model_number, &error_message);
        motor.ledOn(motor_IDs);                              //test
        motor.setNormalDirection(motor_IDs);                 //setReverseDirection
        if ( motor_IDs == 4)
        {
          motor.torqueOn(motor_IDs);
        }
        else
        {
          motor.setMultiTurnControlMode(motor_IDs);
        }    
}

bool tourne_continu_NMBTours(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours)
{

  return 1;
}

bool tourne_continu_NMBTours_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours)
{

  return 1;
}

bool tourne_continu_Torque(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours)
{

  return 1;
}

bool tourne_continu_Torque_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours)
{

  return 1;
}

void stop_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs)
{

}
