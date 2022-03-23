/*
  Project:      CAGIUS
  Description:  Function des actions de la cage
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
                Natael Laroche-Latulippe
*/

#include "action_functions.hpp"
#include "motor_functions.hpp" 

DynamixelWorkbench dyna;

// ========= Functions ========

void init_motors_action()
{
/**
 * Initialisation des moteurs Dynamixel
 * @param { } 
 * @return { void }
 */
  init_motors(dyna);
  Serial.println("1Moteur initialise");
}

// etape 1: ouverture de la trappe de la poubelle
void open_poubelle()
{
/**
 * Action ouverture trappe de la poubelle
 * @param { } 
 * @return { void }
 */
  tourne_Xrad_and_Stop(dyna, MOTOR_POUBELLE_ID_Action, RAD_POUBELLE_Action);
  Serial.println("Poubelle ouverte");
  
}
// etape 2: ouverture des trapes du convoyeur
void open_trappes()
{
/**
 * Action ouverture des trappes du convoyeur
 * @param { } 
 * @return { void }
 */
  tourne_Xrad_and_Stop(dyna, MOTOR_TRAPPES_ID_Action, RAD_TRAPPES_Action);
  Serial.println("Trappes ouvertes");
  
}
// etape 3: convoyeur (avec %)
void convoyeur(int percent)
{
/**
 * Action fonctionnement du convoyeur
 * @param { int } percent         (pourcentage du convoyeur a mettre a la poubelle selon des bonds de 10%)
 * @return { void }
 */
  tourne_continu_NMBTours(dyna, MOTOR_CONVOYEUR_ID_Action, (NMB_TOURS_CONVOYEUR_10percent*(percent/10)));
  Serial.println("Convoyeur fini");
}
// etape 4: fermeture trapes du convoyeur
void close_trappes()
{
/**
 * Action fermeture des trappes du convoyeur
 * @param { } 
 * @return { void }
 */
  tourne_Xrad_ReturnPos(dyna, MOTOR_TRAPPES_ID_Action, RAD_TRAPPES_Action);
  Serial.println("Trappes fermees");
}
// etape 4: fermeture trape de la poubelle
void close_poubelle()
{
/**
 * Action ouverture de la trappe de la poubelle
 * @param { } 
 * @return { void }
 */
  tourne_Xrad_ReturnPos(dyna, MOTOR_POUBELLE_ID_Action, RAD_POUBELLE_Action);
  Serial.println("Poubelle fermee");
}
// etape 5: compression de la litiere
void compression_litiere(int percent)
{
/**
 * Action compression de la litiere selon le torque (force a exercer)
 * @param { int } percent         (pourcentage de compression selon des bonds de 10%, presentement pas utilisé)
 * @return { void }
 */
  tourne_continu_Torque(dyna, MOTOR_VIS_ID_Action, NMB_TORQUE_Compression);
  Serial.println("Compression de la litiere terminee");
}
// etape 6: retour de la pelle
void home_litiere(int percent)
{
/**
 * Action retour compression de la litiere selon le torque (force a exercer)
 * @param { int } percent         (pourcentage de compression selon des bonds de 10%, presentement pas utilisé)
 * @return { void }
 */
  tourne_continu_Torque_goBack(dyna, MOTOR_VIS_ID_Action, NMB_TORQUE_Retour);
  Serial.println("Compresseur de litiere home");
}
