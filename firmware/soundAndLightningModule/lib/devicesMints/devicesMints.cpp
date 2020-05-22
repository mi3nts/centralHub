
#include "devicesMints.h"

// For SEN0232
void readSEN0232Mints(uint8_t pinIn){

    uint8_t rawAnalog = analogRead(pinIn);
    float rawVoltage = (rawAnalog / 1024.0) * 5.0;
    float db = rawVoltage * 50.0;  //convert voltage to decibel value

    String readings[3] = { String(rawAnalog),String(rawVoltage) ,String(db)};
    delay(2);
    sensorPrintMints("SEN0232",readings,3);

}


// For AS3935
bool initializeAS3935Mints(){

  I2c.begin();
  I2c.pullup(true);
  I2c.setSpeed(1);

  delay(2);

  lightning0.setI2CAddress(AS3935_ADD3);

  if(lightning0.defInit() == 0){
    lightning0.powerUp();
    lightning0.setOutdoors();
    lightning0.disturberEn();
    lightning0.setIRQOutputSource(0);
    lightning0.setTuningCaps(AS3935_CAPACITANCE);
    lightning0.setNoiseFloorLvl(2);
    lightning0.setWatchdogThreshold(2);
    lightning0.setSpikeRejection(2);
    Serial.println("AS3935 initiated");
    delay(1);
    return true;
  }
  else{
    Serial.println("AS3935 not found");
    return false;
  }
  // Configure sensor

}

void readAS3935Mints(){

    uint8_t     src   = lightning0.getInterruptSrc();
    uint32_t energy   = lightning0.getStrikeEnergyRaw();
    uint8_t  distance = lightning0.getLightningDistKm();

    String readings[3] = { String(src), String(energy) , String(distance)};
    sensorPrintMints("AS3935",readings,3);

}


