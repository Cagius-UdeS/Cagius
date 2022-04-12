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
 const char *log = NULL;
 
 motor.init(DEVICE_NAME, 57600, &log);
 
        for (int i = 1; i <= 4; ++i)
    {
        const char* motor_name = i+"";
        uint16_t model_number = 0;
        //const char* log;
        //motor.init(motor_name, 57600, &log);

        if (i == 2)   // initialisation moteur trappes
        {
          motor.ping(MOTOR_TRAPPES_ID, &model_number, &log);
          motor.ledOn(MOTOR_TRAPPES_ID);        
          motor.torqueOff(MOTOR_TRAPPES_ID);                       
          motor.setReverseDirection(MOTOR_TRAPPES_ID);                       //setNormalDirection
          motor.jointMode(MOTOR_TRAPPES_ID, V_Trappes, 0, &log);  
          motor.torqueOn(MOTOR_TRAPPES_ID);
          Serial.println("Moteur 1 initialise (TRAPPES)");
        }
        else if (i == 1)   // initialisation moteur poubelle
        {
          motor.ping(MOTOR_POUBELLE_ID, &model_number, &log);
          motor.ledOn(MOTOR_POUBELLE_ID);   
          motor.torqueOff(MOTOR_TRAPPES_ID);                             
          motor.setNormalDirection(MOTOR_POUBELLE_ID);                 //setNormalDirection
          motor.jointMode(MOTOR_POUBELLE_ID, V_Trappes, 0, &log);
          motor.torqueOn(MOTOR_POUBELLE_ID);
          Serial.println("Moteur 2 initialise (POUBELLE)");
        }
        else if (i == 3)   // initialisation moteur convoyeur
        {
          motor.ping(MOTOR_VIS_ID, &model_number, &log);
          motor.ledOn(MOTOR_VIS_ID);   
          //motor.torqueOn(MOTOR_VIS_ID);                              
          //motor.setNormalDirection(MOTOR_VIS_ID);                 //setReverseDirection
          motor.wheelMode(MOTOR_VIS_ID,0, &log);
          Serial.println("Moteur 3 initialise (VIS)");
        }
        else if (i == 4)   // initialisation moteur poubelle
        {
          motor.ping(MOTOR_CONVOYEUR_ID, &model_number, &log);
          motor.ledOn(MOTOR_CONVOYEUR_ID);      
          //motor.torqueOn(MOTOR_CONVOYEUR_ID);                           
          //motor.setNormalDirection(MOTOR_CONVOYEUR_ID);                 //setReverseDirection
          motor.wheelMode(MOTOR_CONVOYEUR_ID,0, &log);
          Serial.println("Moteur 4 initialise (CONVOYEUR)");
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

int tourne_continu_Torque(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_torque, int percent)
{
 /**
 * Fonction de rotation de moteur en continu selon le torque et le courant
 * @param { DynamixelWorkbench& } motor
 * @param { uint8_t } motor_IDs
 * @param { int } nmb_torque
 * @return { int }  ii
 */  
  motor.goalVelocity(motor_IDs, V_Poubelle);
  int ii = 0;
  const char *log = NULL;
  bool result = false;
  int32_t dataC = 0;
  int32_t dataCM = 1193;
  uint16_t model_number = 0;
  motor.ping(motor_IDs, &model_number, &log);
  
  do {
    // statement block 
    dataC = 0;    
    result = motor.readRegister(motor_IDs, "Present_Current", &dataC, &log);
    delay(DELAY_POUBELLE_FREQCALCUL);
    
    Serial.print("I = ");
    Serial.print(UINT16_MAX-dataC);
    Serial.print(" sur ");
    Serial.println(dataCM);

    ii ++;  
  } while ((int32_t)(UINT16_MAX-dataC) <= (int32_t)((dataCM)*PERCENT_MAX_CURRENT) && ii <=  INCREMENT_POUBELLE_MAX); 
  Serial.println(ii);   
  motor.goalVelocity(motor_IDs, 0);
  return ii;
}

bool tourne_continu_Torque_goBack(DynamixelWorkbench&  motor, uint8_t motor_IDs, int nmb_torque,  int percent, int ii)
{
 /**
 * Fonction de rotation de moteur en continu dans la meme sequence que la fonction en torque et courant
 * @param { DynamixelWorkbench& } motor
 * @param { uint8_t } motor_IDs
 * @param { int } nmb_torque
 * @param { int } ii
 * @return { bool }
 */

  motor.goalVelocity(motor_IDs, -V_Poubelle);
  const char *log = NULL;
  bool result = false;
  int32_t dataC = 0;
  int32_t dataCM = 1193;
  uint16_t model_number = 0;
  motor.ping(motor_IDs, &model_number, &log);
  bool SwitchActive = false;
  
  do {
    // statement block   
    dataC = 0;    
    result = motor.readRegister(motor_IDs, "Present_Current", &dataC, &log);
    delay(DELAY_POUBELLE_FREQCALCUL);
    
    Serial.print("I = ");
    Serial.print(dataC);
    Serial.print(" sur ");
    Serial.println(dataCM);
    ii --;  
    //SWITCH ????????
    SwitchActive = false;
    
  } while ((int32_t)(dataC) <= (int32_t)((dataCM)*PERCENT_MAX_CURRENT) && ii >= -10 && SwitchActive == false);
  
  motor.goalVelocity(motor_IDs, 0);

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
 motor.goalPosition(motor_IDs, (int32_t)(PI_SUR_2*nmb_rad));

  Serial.println("Mouvement fini");
  if (nmb_rad == 0)
  {
    delay(DELAY_PI_SUR_2*4);
  }
  else 
  {
    delay(DELAY_PI_SUR_2*nmb_rad);
  }
  return true;  
}

void stop_motors(DynamixelWorkbench&  motor, uint8_t motor_IDs)
{

}

void readCurrent(DynamixelWorkbench&  motor, uint8_t motor_IDs)
{
   uint8_t id = MOTOR_VIS_ID;
        bool result = false;
        int32_t data = 0;
        const char *log = NULL;
        const char *item_nameCurrent = "Present_Current";
        
        result = motor.readRegister(id, item_nameCurrent, &data, &log);
        if (result == false)
        {
          Serial.println(log);
          Serial.println("Failed to read");
          return;
        }
        else
        {
          Serial.println(log);
          Serial.print("read data : ");
          Serial.println(data);
        }
}

void home_motor(DynamixelWorkbench&  motor, uint8_t motor_IDs)
{
 motor.goalPosition(motor_IDs, 0);
  
}
