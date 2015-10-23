#include "shiftRegisteredInput.h"

ShiftRegisteredInput::ShiftRegisteredInput(ShiftRegister* sr, uint8_t firstPin, uint8_t lastPin, uint8_t inputPin)
{
    this->inputPin = getPINPtrForDigital(inputPin);
    this->inputBit = getBITForDigital(inputPin);
    getDDRForDigital(inputPin) &= ~(1<<this->inputBit);
    getPORTForDigital(inputPin) &= ~(1<<this->inputBit);

    this->sr = sr;
    this->firstPin = firstPin;
    this->lastPin = lastPin;
}
int ShiftRegisteredInput::read()
{
    int states = 0;
    int toSend = 1 << this->firstPin;
    uint8_t tab[] = {(toSend & 0xFF00)>>8, toSend&0xFF };
    this->sr->sendBytes(tab, 2);
    for(int i=this->firstPin; i<this->lastPin; i++)
    {
        states |= !!(*this->inputPin & (1<<this->inputBit)) << i;
        this->sr->shift();
        this->sr->storage();
    }
    return states;
}
