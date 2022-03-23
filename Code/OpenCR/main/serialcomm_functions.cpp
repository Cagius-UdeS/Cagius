/*
  Project:      CAGIUS
  Description:  Function Serial Com.
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
                Natael Laroche-Latulippe
*/

#include "serialcomm_functions.hpp"
#include <Arduino.h>
#include <iostream>
#include <string>
#include <vector>

// ========= Functions ========

void comm_init()
{
 /**
 * Initialisation de la communication et attente de connection
 * @param { } 
 * @return { void }
 */
  Serial.begin(BAUDRATE);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
}

String get_msg()
{
 /**
 * Fonction de lecture de message et filtre le device ID du RaspberryPi
 * @param { } 
 * @return { String }
 */
  String temp = Serial.readStringUntil('\n');
  String msg = "";
  // Only read a string of 2 caracter or more, the first caracter is the openCR ID
  if (temp.length() > 1)
  {
    if (temp[0] != OPENCR_ID)
    {
      msg = temp.substring(1);
    }
  }
  return msg;
}

String should_wash(String& state)
{
 /**
 * Fonction de lecture de message et détermine si on nettoie la cage
 * @param { String& } state     // state = message à analyser 3 mots, exemple: {"WASH 80 60"}
 * @return { String }           // retourne deux integer en chaine de caractere, exemple: {"80 60"}
 */

 // séparation du message en vecteur de 3 string
  String words[3];
  String out;
  int StringCount = 0;

  while (state.length() > 0)
  {
    int index = state.indexOf(' ');
    if (index == -1) // No space found
    {
      words[StringCount++] = state;
      break;
    }
    else
    {
      words[StringCount++] = state.substring(0, index);
      state = state.substring(index+1);
    }
  }

  // lecture du premier mot et vérification de s'il est égal a WASH
  if (words[0] == "WASH")
  { 
    out = words[1] + " " + words[2];
    return out;
  }
  else
  {
    return out;
  }
  
}

bool should_trash(String& state)
{
 /**
 * Fonction de lecture de message et détermine si on nettoie la poubelle
 * @param { String& } state     // state = message à analyser 1 mots, exemple: {"TRASH"}
 * @return { bool }     
 */
  if (state == "TRASH")
  {
    return true;
  }
  else
  {
    return false;
  }
   
}

String send_msg(const String& msg)
{
 /**
 * Fonction de lecture de message et détermine si on nettoie la cage
 * @param { String& } state     // state = message à analyser 3 mots, exemple: {"WASH 80 60"}
 * @return { String }           // retourne deux integer en chaine de caractere, exemple: {"80 60"}
 */
  String msg_envoye = OPENCR_ID + msg;
  Serial.println(msg_envoye);
  return msg_envoye;
}

bool should_start(const String& state)
{
 /**
 * Fonction de lecture de message et détermine si on active la cage
 * @param { String& } state     // state = message à analyser 1 mots, exemple: {"START"}
 * @return { bool }     
 */
  if (state == "START")
  {
    return true;
  }
  else
  {
    return false;
  }
}

bool should_end(const String& state)
{
 /**
 * Fonction de lecture de message et détermine si on désactive la cage
 * @param { String& } state     // state = message à analyser 1 mots, exemple: {"END"}
 * @return { bool }     
 */
  if (state == "END")
  {
    return true;
  }
  else
  {
    return false;
  }
}
