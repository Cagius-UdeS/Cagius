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
          //motor.setPositionControlMode(MOTOR_TRAPPES_ID, &error_message);
          motor.jointMode(MOTOR_TRAPPES_ID, V_Trappes, 0, &error_message);
          motor.torqueOn(MOTOR_TRAPPES_ID);
          Serial.println("1Moteur 1 initialise (TRAPPES)");
        }
        else if (i == 2)
        {
          motor.ping(MOTOR_POUBELLE_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_POUBELLE_ID);                              //test
          motor.setNormalDirection(MOTOR_POUBELLE_ID);                 //setReverseDirection
          //motor.setPositionControlMode(MOTOR_POUBELLE_ID, &error_message);
          motor.jointMode(MOTOR_POUBELLE_ID, V_Trappes, 0, &error_message);
          motor.torqueOn(MOTOR_POUBELLE_ID);
          Serial.println("1Moteur 2 initialise (POUBELLE)");
        }
        else if (i == 3)
        {
          motor.ping(MOTOR_CONVOYEUR_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_CONVOYEUR_ID);                              //test
          motor.setNormalDirection(MOTOR_CONVOYEUR_ID);                 //setReverseDirection
          motor.wheelMode(MOTOR_CONVOYEUR_ID,0, &error_message);
          //motor.torqueOn(MOTOR_CONVOYEUR_ID);
          Serial.println("1Moteur 3 initialise (CONVOYEUR)");
        }
        else if (i == 4)
        {
          motor.ping(MOTOR_VIS_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_VIS_ID);                              //test
          motor.setNormalDirection(MOTOR_VIS_ID);                 //setReverseDirection
          motor.setTorqueControlMode(MOTOR_VIS_ID, &error_message);
          motor.torqueOn(MOTOR_VIS_ID);
          Serial.println("1Moteur 4 initialise (VIS)");
        }
    }
}

bool tourne_continu_NMBTours(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours)
{
  motor.goalVelocity(motor_IDs, V_Convoyeur);
  delay(nmb_tours*TIME_PER_TROURS);
  motor.goalVelocity(motor_IDs, 0);
  return true;
}

bool tourne_continu_NMBTours_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours)
{
  //ne devrait pas etre utilisée, le convoyeur n'a pas de position initiale juste un zero a vitesse = 0
  return true;
}

bool tourne_continu_Torque(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_torque)
{

  return true;
}

bool tourne_continu_Torque_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours)
{

  return true;
}

bool tourne_Xrad_and_Stop(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad)
{
  
  int32_t pos = 1023*nmb_rad;

  motor.goalPosition(motor_IDs, pos); 

  Serial.println("1Mouvement fini");
  delay(4000);

  return true;  
}

bool tourne_Xrad_ReturnPos(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad)
{
  //motor.setReverseDirection(motor_IDs);                 //setNormalDirection
  motor.goalPosition(motor_IDs, (int32_t)0);   //possiblement pos ???

  Serial.println("1Mouvement fini");

  //motor.setNormalDirection(motor_IDs);
  delay(4000);
  
  return true;  
}

void stop_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs)
{

}
