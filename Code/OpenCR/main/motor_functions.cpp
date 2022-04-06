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
/**
 * Initialisation des moteurs Dynamixel et sélection du mode de fonctionnemnet
 * @param { DynamixelWorkbench& } motor
 * @return { void }
 */
 
        for (int i = 1; i <= 4; ++i)
    {
        const char* motor_name = i+"";
        uint16_t model_number = 0;
        const char* error_message;
        motor.init(motor_name, 57600, &error_message);

        if (i == 2)   // initialisation moteur trappes
        {
          motor.ping(MOTOR_TRAPPES_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_TRAPPES_ID);        
          motor.torqueOff(MOTOR_TRAPPES_ID);                       
          motor.setReverseDirection(MOTOR_TRAPPES_ID);                       //setNormalDirection
          motor.jointMode(MOTOR_TRAPPES_ID, V_Trappes, 0, &error_message);  
          motor.torqueOn(MOTOR_TRAPPES_ID);
          Serial.println("Moteur 1 initialise (TRAPPES)");
        }
        else if (i == 1)   // initialisation moteur poubelle
        {
          motor.ping(MOTOR_POUBELLE_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_POUBELLE_ID);   
          motor.torqueOff(MOTOR_TRAPPES_ID);                             
          motor.setNormalDirection(MOTOR_POUBELLE_ID);                 //setNormalDirection
          motor.jointMode(MOTOR_POUBELLE_ID, V_Trappes, 0, &error_message);
          motor.torqueOn(MOTOR_POUBELLE_ID);
          Serial.println("Moteur 2 initialise (POUBELLE)");
        }
        else if (i == 4)   // initialisation moteur convoyeur
        {
          motor.ping(MOTOR_CONVOYEUR_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_CONVOYEUR_ID);                              
          motor.setNormalDirection(MOTOR_CONVOYEUR_ID);                 //setReverseDirection
          motor.wheelMode(MOTOR_CONVOYEUR_ID,0, &error_message);
          Serial.println("Moteur 3 initialise (CONVOYEUR)");
        }
        else if (i == 3)   // initialisation moteur poubelle
        {
          motor.ping(MOTOR_VIS_ID, &model_number, &error_message);
          motor.ledOn(MOTOR_VIS_ID);                              
          motor.setNormalDirection(MOTOR_VIS_ID);                 //setReverseDirection
          motor.setTorqueControlMode(MOTOR_VIS_ID, &error_message);
          motor.torqueOn(MOTOR_VIS_ID);
          Serial.println("Moteur 4 initialise (VIS)");
        }
    }
}

bool tourne_continu_NMBTours(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_tours)
{
 /**
 * Fonction de rotation de moteur en continu selon le nombre de tour et vitesse de rotation
 * @param { DynamixelWorkbench& } motor
 * @param { uint8_t } motor_IDs
 * @param { int } nmb_tours
 * @return { bool }
 */
  motor.goalVelocity(motor_IDs, V_Convoyeur);
  delay(nmb_tours*TIME_PER_TROURS);           // temps que prend un tour avec la vitesse definie dans les constantes
  motor.goalVelocity(motor_IDs, 0);
  return true;
}

bool tourne_continu_Torque(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_torque, int percent)
{
 /**
 * Fonction de rotation de moteur en continu selon le torque et le courant
 * @param { DynamixelWorkbench& } motor
 * @param { uint8_t } motor_IDs
 * @param { int } nmb_torque
 * @return { bool }
 */
  //motor.goalCurrent(motor_IDs, nmb_torque);

  //Serial.println("Mouvement fini");
  //delay(DELAY_CONV_10Percent*percent/10);
 
  return true;
}

bool tourne_continu_Torque_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_torque,  int percent)
{
 /**
 * Fonction de rotation de moteur en continu dans la meme sequence que la fonction en torque et courant
 * @param { DynamixelWorkbench& } motor
 * @param { uint8_t } motor_IDs
 * @param { int } nmb_torque
 * @return { bool }
 */

  //motor.setReverseDirection(motor_IDs);
  //motor.goalCurrent(motor_IDs, nmb_torque);

  //Serial.println("Mouvement fini");
  //delay(DELAY_CONV_10Percent*percent/10);
  
  //motor.setNormalDirection(motor_IDs);

  return true;
}

bool tourne_Xrad_and_Stop(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad)
{
 /**
 * Fonction de rotation de moteur en position
 * @param { DynamixelWorkbench& } motor
 * @param { uint8_t } motor_IDs
 * @param { float } nmb_rad
 * @return { bool }
 */
  // position a atteindre avec position a pi/2 et nombre de pi/2 a se déplacer
  int32_t pos = PI_SUR_2*nmb_rad;

  motor.goalPosition(motor_IDs, pos); 
 
  delay(DELAY_PI_SUR_2*nmb_rad);
  Serial.println("Mouvement fini");
  
  return true;  
}

bool tourne_Xrad_ReturnPos(DynamixelWorkbench&  motor, uint8_t motor_IDs, float nmb_rad, uint8_t elmt)
{
 /**
 * Fonction de rotation de moteur retour a position home
 * @param { DynamixelWorkbench& } motor
 * @param { uint8_t } motor_IDs
 * @param { float } nmb_rad
 * @return { bool }
 */
 if (elmt == ELMT_POUBELLE)
 {
  motor.goalPosition(motor_IDs, HOME_POUBELLE);
 }

 if (elmt == ELMT_TRAPPES)
 {
  motor.goalPosition(motor_IDs, HOME_TRAPPES);
 }

  Serial.println("Mouvement fini");
  delay(DELAY_PI_SUR_2*nmb_rad);
  
  return true;  
}

void stop_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs)
{

}
