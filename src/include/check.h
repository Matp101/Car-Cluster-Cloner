#include "../src/config.h"

#ifndef CHIP
  #error "CHIP is not defined"
#elif CHIP!=46 && CHIP!=56 && CHIP!=66 && CHIP!=76 && CHIP!=86
  #define EEPROM_SIZE 0
  #error "CHIP is not valid, must be 46, 56, 66, 76, or 86"
#endif

#ifndef ORG
  #error "ORG is not defined"
#elif ORG!=8 && ORG!=16
  #define EEPROM_SIZE 0
  #error "ORG is not valid, must be 8 or 16"
#endif


