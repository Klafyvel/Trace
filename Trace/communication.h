#ifndef H_COMMUNICATION
#define H_COMMUNICATION

#include "settings.h"

#ifdef DEBUG
#define dvar(var) Serial.print(#var);Serial.print(" : ");Serial.println(var)
#define dvarbin(var) Serial.print(#var);Serial.print(" : ");Serial.println(var, BIN)
#define dinfo(info) Serial.println(info)
#else
#define dvar(var)
#define dinfo(info)
#endif

#define error(msg) Serial.print("Error : ");Serial.println(msg)

#define pchar(c) Serial.print(c)

#endif
