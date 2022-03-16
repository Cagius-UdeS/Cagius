/*
  Project:      CAGIUS
  Description:  Function Motor
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
                Natael Laroche-Latulippe
*/

#include "motor_functions.hpp"
#include <Arduino.h>

// ========= Functions ========

void init_motors(DynamixelWorkbench& motor)
{

        for (int i = 1; i <= 4; ++i)
    {
        const char* motor_name = i+"";
        uint16_t model_number = 0;
        const char* error_message;
        motor.init(motor_name, 57600, &error_message);

        if (i == 1)
        {
          motor.ping(MOTOR_TRAPPES_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_TRAPPES_ID);                              //test
          motor.setNormalDirection(MOTOR_TRAPPES_ID);                 //setReverseDirection
          motor.setPositionControlMode(MOTOR_TRAPPES_ID, &error_message);
          //motor.torqueOn(MOTOR_TRAPPES_ID);
        }
        else if (i == 2)
        {
          motor.ping(MOTOR_POUBELLE_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_POUBELLE_ID);                              //test
          motor.setNormalDirection(MOTOR_POUBELLE_ID);                 //setReverseDirection
          motor.setPositionControlMode(MOTOR_POUBELLE_ID, &error_message);
          //motor.torqueOn(MOTOR_POUBELLE_ID);
        }
        else if (i == 3)
        {
          motor.ping(MOTOR_CONVOYEUR_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_CONVOYEUR_ID);                              //test
          motor.setNormalDirection(MOTOR_CONVOYEUR_ID);                 //setReverseDirection
          motor.setVelocityControlMode(MOTOR_CONVOYEUR_ID, &error_message);
          //motor.torqueOn(MOTOR_CONVOYEUR_ID);
        }
        else if (i == 4)
        {
          motor.ping(MOTOR_VIS_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_VIS_ID);                              //test
          motor.setNormalDirection(MOTOR_VIS_ID);                 //setReverseDirection
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

bool tourne_continu_Torque(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_torque)
{

  return 1;
}

bool tourne_continu_Torque_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours)
{

  return 1;
}

float tourne_Xrad_and_Stop(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad)
{
  motor.torqueOn(motor_IDs);
  
  bool move_complete = false;
  motor.goalPosition(motor_IDs, nmb_rad); 
  float nmb_rad_temp = 0.0;

  while ( move_complete != true )
  {
    motor.getRadian(motor_IDs, &nmb_rad_temp);
    if (abs(nmb_rad_temp - nmb_rad) < DELTA_RAD)
    {
      move_complete = true;
    }
    delay(10);
  }

  return nmb_rad;  
}

bool tourne_Xrad_ReturnPos(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad)
{
  bool move_complete = false;
  motor.goalPosition(motor_IDs, 0);   //possiblement -nmb_rad ???
  float nmb_rad_temp = 0.0;

  while ( move_complete != true )
  {
    motor.getRadian(motor_IDs, &nmb_rad_temp);
    if (abs(nmb_rad_temp) < DELTA_RAD)
    {
      move_complete = true;
      motor.torqueOff(motor_IDs);
    }
    delay(10);
  }

  
  return 1;  
}

void stop_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs)
{

}
