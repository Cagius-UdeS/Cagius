/*
Project:      CAGIUS
Description:  Header: Function Action de la cage
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

//uint8_t get_id[16];
//uint8_t scan_cnt = 0;
//uint8_t ping_cnt = 0;
const uint8_t MOTOR_TRAPPES_ID_Action = 1;
const uint8_t MOTOR_POUBELLE_ID_Action = 2;
const uint8_t MOTOR_CONVOYEUR_ID_Action = 3;
const uint8_t MOTOR_VIS_ID_Action = 4;

const float RAD_TRAPPES_Action = 2;
const float RAD_POUBELLE_Action = 1;
const float NMB_TOURS_CONVOYEUR_10percent = 5.2;
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
void compression_litiere(void);
// etape 6: retour de la pelle
void home_litiere(void);




#endif
