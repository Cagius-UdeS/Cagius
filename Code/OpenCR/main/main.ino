/*
  Project:      CAGIUS
  Description:  Main of the OpenCR.
  Authors:      Florence Millette
              Aissatou
              Alexandre
              Laurie Croteau
              Natael Laroche-Latulippe
*/

// ========= Libraries ========
#include <Arduino.h>
#include <stdint.h>
#include <DynamixelWorkbench.h>
#include <vector>
#include "serialcomm_functions.hpp"
#include "motor_functions.hpp"
#include "action_functions.hpp"

// ========= Constant =========



//----------motor--------------

#if defined(__OPENCM904__)
  #define DEVICE_NAME "3" //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP
#elif defined(__OPENCR__)
  #define DEVICE_NAME ""
#endif  


// ========= Enumerations =====

enum State {
  Off, // attente du start de la cage
  Wait, // en attente de message de la camera
  Washing, // cycle de nettoyage
  Trash, // nettoyage de la poubelle, donc uniquement vis sans fin
};

// ========= Constant =========

 

// ========= Variables ========

enum State current_state;
String msg;
//DynamixelWorkbench dyna;
int percent[2];

// ========= Functions ========

void setup() {
  // put your setup code here, to run once:
  comm_init();
  current_state = Off;
  init_motors_action();
}

void loop() {
  // put your main code here, to run repeatedly:
  switch (current_state) {
    case Off:
    {
      // waiting for the start signal
      send_msg("En attente du lancement de la cage");
      msg = get_msg();
      if (should_start(msg) == true)
      {
        send_msg("Cage armee");
        current_state = Wait;
      }

      break;
  }
      
    case Wait:
    {
      // Waiting for the Camera or the stop of the cage signal
      send_msg("En attente dinstruction");
      msg = get_msg();

      // pi dit stop
      if (should_end(msg) == true)
      {
        send_msg("Cage arretee");
        current_state = Off;
        break;
      }

      // statement sur la camera (envoye du pi)
      String temporaire1 = should_wash(msg);

      String words1[3];
      int StringCount1 = 0;

      while (temporaire1.length() > 0)
      {
        int index = temporaire1.indexOf(' ');
        if (index == -1) // No space found
        {
          words1[StringCount1++] = temporaire1;
          break;
        }
        else
        {
          words1[StringCount1++] = temporaire1.substring(0, index);
          temporaire1 = temporaire1.substring(index+1);
        }
      }
      
      percent[0] = words1[0].toInt();
      percent[1] = words1[1].toInt();
      
      if (percent[1] != 0)
      {
        send_msg("Nettoyage amorcé a " + String(percent[0]) + " percent");
        current_state = Washing;
      }

      if (should_trash(msg) == true)
      {
        current_state = Trash;
      }

      break;
  }
      
    case Washing:
    {
    
      // nettoyage de la cage
      send_msg("Nettoyage en cours");

      // etape 1: ouverture de la trappe de la poubelle
      open_poubelle();
      // etape 2: ouverture des trapes du convoyeur
      open_trappes();
      // etape 3: convoyeur (avec %)
      convoyeur(percent[0]);
      // etape 4: fermeture trapes du convoyeur
      close_trappes();
      // etape 4: fermeture trape de la poubelle
      close_poubelle();
      // etape 5: compression de la litiere
      compression_litiere(percent[1]);
      // etape 6: retour de la pelle
      home_litiere(percent[1]);
      
      send_msg("Nettoyage fini");
      current_state = Wait;
      break;
  }

    case Trash:
    {

      compression_litiere(100);

      home_litiere(100);

      send_msg("Nettoyage de la poubelle fini");
      current_state = Wait;

      break;
    }
  }

}
