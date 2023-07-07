#include <Arduino.h>
#include <M93Cx6.h>
#include "config.h"
#include "check.h"
#include "setup.h"

/******************************************************************************
 **
 **  M93Cx6 Test Program
 **
 **  Pin-Out:
 **                       _____
 **  Chip Select (cs)  --|1   8|--  (pwr) Vcc
 ** Serial Clock (sk)  --|2   7|--
 **      Data In (di)  --|3   6|--  (org) Organization Select
 **     Data Out (do)  --|4   5|--  (gnd) Vss/Ground
 **                       -----
 **
 *****************************************************************************/

// Source Pin Definitions
#define S_PWR_PIN 3
#define S_CS_PIN 7
#define S_SK_PIN 6
#define S_DI_PIN 5
#define S_DO_PIN 4
#define S_ORG_PIN 2

// Destination Pin Definitions
#define D_PWR_PIN 9
#define D_CS_PIN 10
#define D_SK_PIN 13
#define D_DI_PIN 11
#define D_DO_PIN 12
#define D_ORG_PIN 8

void readEEPROM(M93Cx6 &eeprom, String name);
void transferEEPROM(M93Cx6 &src, M93Cx6 &dst);

M93Cx6 srceeprom = M93Cx6(S_PWR_PIN, S_CS_PIN, S_SK_PIN, S_DO_PIN, S_DI_PIN, S_ORG_PIN);
M93Cx6 dsteeprom = M93Cx6(D_PWR_PIN, D_CS_PIN, D_SK_PIN, D_DO_PIN, D_DI_PIN, D_ORG_PIN);

void setup()
{

  // setup LED_BUILTIN as output
  pinMode(LED_BUILTIN, OUTPUT);

  // Setup Serial
  Serial.begin(9600);
  Serial.println(" ");
  Serial.println("STARTING CLONING PROCESS...");

  // Setup EEPROMs
  srceeprom.setChip(CHIP); // set chip 93C56
  srceeprom.setOrg(ORG);   // 8-bit data organization
  dsteeprom.setChip(CHIP); // set chip 93C56
  dsteeprom.setOrg(ORG);   // 8-bit data organization

  // Show EEPROM contents before cloning
  Serial.println("PREVIOUS DATA:");
  readEEPROM(srceeprom, "SOURCE EEPROM");
  readEEPROM(dsteeprom, "DESTINATION EEPROM");

  // clone EEPROM
  Serial.println(" ");
  Serial.println("CLONING DATA...");
  transferEEPROM(srceeprom, dsteeprom);

  // Show EEPROM contents after cloning
  Serial.println(" ");
  Serial.println("CURRENT DATA:");
  readEEPROM(srceeprom, "SOURCE EEPROM");
  readEEPROM(dsteeprom, "DESTINATION EEPROM");

  Serial.println("PROGRAM DONE!!!");
  Serial.flush();
  delay(200);
  Serial.end();
}

void loop()
{
  // flash LED_BUILTIN to indicate program is Done
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}

void readEEPROM(M93Cx6 &eeprom, String name)
{
  Serial.println("EEPROM DATA FROM " + name + ":");
  int i = 0;
  uint16_t r;

  // Power Up EEPROM
  eeprom.powerUp();
  delay(500);

  //  read string from eeprom and print it
  int lineCount = 0;
  char buffer[24];
  sprintf(buffer, "%5d", lineCount * 16);
  Serial.print(buffer);
  for (i = 0; i < EEPROM_SIZE; i++)
  {
    r = eeprom.read(i);
    #if ORG==16
      sprintf(buffer, " %04X", r);
    #elif ORG==8
      sprintf(buffer, " %02X", r);
    #endif
    Serial.print(buffer);
    if (i % 16 == 15)
    {
      if ((lineCount+1)*16 == EEPROM_SIZE)
        break;
      Serial.println("");
      sprintf(buffer, "%5d", ++lineCount * 16);
      Serial.print(buffer);
    }
    else if (i % 4 == 3)
    {
      Serial.print(" ");
    }
  }

  // Power Down EEPROM
  delay(200);
  eeprom.powerDown();
  delay(500);
  Serial.println(" ");
  Serial.println("DONE!");

}

void transferEEPROM(M93Cx6 &src, M93Cx6 &dst)
{
  Serial.println("EEPROM TRANSFER:");
  int i = 0;
  uint16_t r;
  int lineCount = 0;
  char buffer[24];

  // Power Up EEPROMs
  src.powerUp();
  dst.powerUp();
  dst.writeEnable();
  delay(500);

  //  read string from eeprom and print it
  sprintf(buffer, "%5d", lineCount * 16);
  Serial.print(buffer);
  for (i = 0; i < EEPROM_SIZE; i++)
  {
    r = src.read(i);
    dst.write(i, r);
    #if ORG==16
      sprintf(buffer, " %04X", r);
    #elif ORG==8
      sprintf(buffer, " %02X", r);
    #endif
    Serial.print(buffer);
    if (i % 16 == 15)
    {
      if ((lineCount+1)*16 == EEPROM_SIZE)
        break;
      Serial.println("");
      sprintf(buffer, "%5d", ++lineCount * 16);
      Serial.print(buffer);
    }
    else if (i % 4 == 3)
    {
      Serial.print(" ");
    }
  }
  // Disable write to EEPROM
  delay(200);
  dst.writeDisable();

  // Power Down EEPROMs
  delay(200);
  dst.powerDown();
  src.powerDown();
  delay(500);
  Serial.println(" ");
  Serial.println("DONE!");
}