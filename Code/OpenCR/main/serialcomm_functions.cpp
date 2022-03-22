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
  Serial.begin(BAUDRATE);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
}

String get_msg()
{
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

int should_trash(String& state)
{
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
  String msg_envoye = OPENCR_ID + msg;
  Serial.println(msg_envoye);
  return msg_envoye;
}

bool should_start(const String& state)
{
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
  if (state == "END")
  {
    return true;
  }
  else
  {
    return false;
  }
}
