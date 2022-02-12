/*
  Project:      CAGIUS
  Description:  Header: Function Serial Com.
  Authors:      Florence Millette
                Aissatou
                Alexandre
                Laurie Croteau
*/

#ifndef serailcomm_functions_h
#define serialcomm_functions_h

class String;

// ========= Functions prototype ========

void comm_init();

bool should_start(const String& state);

bool should_end(const String& state);

String get_msg();

String send_msg(const String& msg);


#endif
