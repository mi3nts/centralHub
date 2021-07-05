#ifndef DEVICES_MINTS_H
#define DEVICES_MINTS_H


#include <Arduino.h>

#include "DFRobot_AS3935_I2C.h"
#include <Lib_I2C.h>
#include "jobsMints.h"

// For SEN0232
void readSEN0232Mints(uint8_t pinIn);

// For AS3935
#define AS3935_CAPACITANCE   96
#define AS3935_I2C_ADDR       AS3935_ADD3
extern DFRobot_AS3935_I2C  lightning0;
bool initializeAS3935Mints();
void readAS3935Mints();

#endif
