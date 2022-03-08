/*
  Project:      CAGIUS
  Description:  Function Motor
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
*/

#include "motor_functions.hpp"
#include <Arduino.h>

// ========= Functions ========

bool isAvailableID(uint8_t id)
{
  for (int dxl_cnt = 0; dxl_cnt < (scan_cnt + ping_cnt); dxl_cnt++)
  {
    if (get_id[dxl_cnt] == id)
      return true;
  }

  return false;
}
