/*
  Project:      CAGIUS
  Description:  Header: Function Motor
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
*/

#ifndef motor_functions_h
#define motor_functions_h

// ========= Constant =========

uint8_t get_id[16];
uint8_t scan_cnt = 0;
uint8_t ping_cnt = 0;

// ========= Variables =========

class DynamixelWorkbench;

// ========= Functions prototype ========

bool isAvailableID(uint8_t id);
