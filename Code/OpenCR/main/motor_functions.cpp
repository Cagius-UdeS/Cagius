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

void init_motors(DynamixelWorkbench& motor)
{
        const char* motor_name = 1+"";
        uint16_t model_number = 0;
        const char* error_message;
        motor.init(motor_name, 57600, &error_message);
        motor.ping(motor_IDs, &model_number, &error_message);
        motor.ledOn(motor_IDs);                              //test
        motor.setNormalDirection(motor_IDs);                 //setReverseDirection
        motor.  


        for (int i = 1; i <= 4; ++i)
    {
        const char* motor_name = i+"";
        uint16_t model_number = 0;
        const char* error_message;
        motor.init(motor_name, 57600, &error_message);

        if (i == 1)
        {
          motor.ping(MOTOR_TRAPPES_ID, &model_number, &error_message);
          motor.setPositionControlMode(MOTOR_TRAPPES_ID, &error_message);
          //motor.torqueOn(MOTOR_TRAPPES_ID);
        }
        else if (i == 2)
        {
          motor.ping(MOTOR_POUBELLE_ID, &model_number, &error_message);
          motor.setPositionControlMode(MOTOR_POUBELLE_ID, &error_message);
          //motor.torqueOn(MOTOR_POUBELLE_ID);
        }
        else if (i == 3)
        {
          motor.ping(MOTOR_CONVOYEUR_ID, &model_number, &error_message);
          motor.setVelocityControlMode(MOTOR_CONVOYEUR_ID, &error_message);
          //motor.torqueOn(MOTOR_CONVOYEUR_ID);
        }
        else if (i == 4)
        {
          motor.ping(MOTOR_VIS_ID, &model_number, &error_message);
          motor.setTorqueControlMode(MOTOR_VIS_ID, &error_message);
          //motor.torqueOn(MOTOR_VIS_ID);
        }
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
