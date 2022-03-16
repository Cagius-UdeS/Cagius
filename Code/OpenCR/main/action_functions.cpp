/*
  Project:      CAGIUS
  Description:  Function Action de la cage
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
*/

#include "action_functions.hpp"
#include "motor_functions.hpp" 

DynamixelWorkbench dyna;

// ========= Functions ========

void init_motors_action(void)
{
  init_motors(dyna);
}

// etape 1: ouverture de la trappe de la poubelle
void open_poubelle()
{
  
  
}
// etape 2: ouverture des trapes du convoyeur
void open_trappes()
{
  tourne_Xrad_and_Stop(dyna, MOTOR_TRAPPES_ID_Action, RAD_TRAPPES_Action);
  
}
// etape 3: convoyeur (avec %)
void convoyeur(int percent)
{

  
}
// etape 4: fermeture trapes du convoyeur
void close_trappes()
{
  
  
}
// etape 4: fermeture trape de la poubelle
void close_poubelle()
{

  
}
// etape 5: compression de la litiere
void compression_litiere()
{

  
}
// etape 6: retour de la pelle
void home_litiere()
{

  
}
