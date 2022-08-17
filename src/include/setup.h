#include "../src/config.h"

#ifdef CHIP
  #if CHIP == 46
    #if ORG == 8
      #define EEPROM_SIZE 128
    #elif ORG == 16
      #define EEPROM_SIZE 64
    #endif
  #elif CHIP == 56
    #if ORG == 8
      #define EEPROM_SIZE 256
    #elif ORG == 16
      #define EEPROM_SIZE 128
    #endif
  #elif CHIP == 66
    #if ORG == 8
      #define EEPROM_SIZE 512
    #elif ORG == 16
      #define EEPROM_SIZE 256
    #endif
  #elif CHIP == 76
    #if ORG == 8
      #define EEPROM_SIZE 1024
    #elif ORG == 16
      #define EEPROM_SIZE 512
    #endif
  #elif CHIP == 86
    #if ORG == 8
      #define EEPROM_SIZE 2048
    #elif ORG == 16
      #define EEPROM_SIZE 1024
    #endif
  #endif
#endif