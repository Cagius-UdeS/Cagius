/*
Project:      CAGIUS
Description:  Header: Function des actions de la cage
Authors:      Florence Millette
              Aissatou
              Alexandre
              Laurie Croteau
              Natael Laroche-Latulippe
*/

#ifndef action_functions_h
#define action_functions_h

#include <Arduino.h>
#include <stdint.h>
#include <DynamixelWorkbench.h> 
#include <vector>

// ========= Constant =========

//----------motor--------------
const uint8_t MOTOR_TRAPPES_ID_Action = 2;
const uint8_t MOTOR_POUBELLE_ID_Action = 1;
const uint8_t MOTOR_CONVOYEUR_ID_Action = 3;
const uint8_t MOTOR_VIS_ID_Action = 4;

//----------utilisateion--------------
const float RAD_TRAPPES_Action = 2.5;           // nombre de pi/2 necessaire pour l'ouverture des trappes
const float RAD_POUBELLE_Action = 4;
const int NMB_TOURS_CONVOYEUR_10percent = 1;  // nombre de tour nécessaire au convoyeur pour faire 10%  

const float NMB_TORQUE_Retour = 0.02;
const float NMB_TORQUE_Compression = 0.02;




// ========= Functions prototype ========

void init_motors_action(void);

// etape 1: ouverture de la trappe de la poubelle
void open_poubelle(void);
// etape 2: ouverture des trapes du convoyeur
void open_trappes(void);
// etape 3: convoyeur (avec %)
void convoyeur(int percent);
// etape 4: fermeture trapes du convoyeur
void close_trappes(void);
// etape 4: fermeture trape de la poubelle
void close_poubelle(void);
// etape 5: compression de la litiere
int compression_litiere(int percent);
// etape 6: retour de la pelle
void home_litiere(int percen, int ii);

void read_MotorVisCurrent(void);

void home_motorAction1();
void home_motorAction2();


#endif
