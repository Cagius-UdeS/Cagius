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

// ========= Enumerations =====

enum State
{
  Init,
  Off,     // attente du start de la cage
  Wait,    // en attente de message de la camera
  Washing, // cycle de nettoyage
  Trash,   // nettoyage de la poubelle, donc uniquement vis sans fin
  Test
};

// ========= Constant =========

// ========= Variables ========

enum State current_state;
String msg;       // messsage lu du Pi
int tier[2];
int ii;

// ========= Functions ========

void setup()
{
  // put your setup code here, to run once:
  comm_init();

  pinMode(1,OUTPUT);
  digitalWrite(1,HIGH);

  current_state = Init;
}

void loop()
{
  // put your main code here, to run repeatedly:
  switch (current_state)
  {
    
  case Init:
  {
    msg = get_msg();
    if (should_init(msg) == true)
    {
      init_motors_action();
      current_state = Off;
      send_msg("En attente du lancement de la cage");
      break;
    }
    break;
  }    
  case Off:
  {
    // waiting for the start signal, if received, state = Wait
    // send_msg("En attente du lancement de la cage");
    msg = get_msg();
    if (should_start(msg) == true)
    {
      send_msg("Cage armee");
      current_state = Wait;
      send_msg("En attente dinstruction");
      break;
    }
    if (msg == "TEST")
    {
      current_state = Test;
      send_msg("Mode Test");
      break;
    }

    break;
  }

  case Wait:
  {
    // Waiting for the Pi to send the instruction Wash, Trash or the stop of the cage signal
    msg = get_msg();

    // pi dit stop
    if (should_end(msg) == true)
    {
      send_msg("Cage arretee");
      current_state = Off;
      break;
    }

    // pi dit de débuter le nettoyage de ta poubelle
    if (should_trash(msg) == true)
    {
      current_state = Trash;
      break;
    }

    // statement sur la camera (envoye du pi), lecture de deux int, premier %
    // de la cage a nettoyer (convoyeur), second % de la poubelle a compresser

    // séparation du string qui est recu en deux integer entre 0 et 100
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
        temporaire1 = temporaire1.substring(index + 1);
      }
    }

    tier[0] = words1[0].toInt();
    tier[1] = words1[1].toInt();

    if (tier[0] != 0 && tier[1] != 0)
    {
      send_msg("Nettoyage amorcé a " + String(tier[0]) + " tier de convoyeur et " + String(tier[1]) + " pourcent de poubelle"); // message feedback
      current_state = Washing;
      break;
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
    //close_trappes();
    // etape 3: convoyeur (avec %)
    convoyeur(tier[0]);
    // etape 4: fermeture trapes du convoyeur
    close_trappes();
    //open_trappes();
    // etape 4: fermeture trape de la poubelle
    close_poubelle();
    // etape 5: compression de la litiere
    int ii = compression_litiere(tier[1]);
    // etape 6: retour de la pelle
    home_litiere(tier[1], ii);

    send_msg("Nettoyage fini");
    current_state = Wait;
    send_msg("En attente dinstruction");
    break;
  }

  case Trash:
  {
    // nettoyage de la poubelle (compression de la litiere a la limite de la boite, car utilisateur met un sac a la sortie
    send_msg("Nettoyage de la poubelle amorce");
    int ii = compression_litiere(100);

    home_litiere(100, ii);

    send_msg("Nettoyage de la poubelle fini");
    current_state = Wait;
    send_msg("En attente dinstruction");

    break;
  }
  case Test:
  {
    
    msg = get_msg();
    if (msg == "OpenTrappes")
    {
      open_trappes();
    }
    if (msg == "CloseTrappes")
    {
      close_trappes();
    }
    if (msg == "OpenPoubelle")
    {
      open_poubelle();
    }
    if (msg == "ClosePoubelle")
    {
      close_trappes();
    }
    if (msg == "Convoyeur10")
    {
      convoyeur(1);
    }
    if (msg == "Convoyeur100")
    {
      convoyeur(3);
    }
    if (msg == "Litiere10")
    {
      ii = compression_litiere(10);
    }
    if (msg == "Litiere100")
    {
      ii = compression_litiere(100);
    }
    if (msg == "LitiereRetour10")
    {
      home_litiere(10, ii);
    }
    if (msg == "LitiereRetour100")
    {
      home_litiere(100, ii);
    } 
    if (msg == "HomePoubelle")
    {
      home_motorAction1();
    }
    if (msg == "HomeTrappes")
    {
      home_motorAction2();
    }
    if (msg == "ReadVis")
    {
      read_MotorVisCurrent();
    }
    
    if (msg == "Off")
    {
      current_state = Off;
      send_msg("Cage mode Off");
      break;
    }

    
    break;
  } 
}
}
