#ifndef H_SHIFT_REGISTERED_INPUT
#define H_SHIFT_REGISTERED_INPUT

#include "Arduino.h"

#include "ShiftRegister/shiftRegister.h"
#include "communication.h"



/* ShiftRegisterInput returns the state of input on a shift register.
 * here's for two shift register (74H595, so 8 possible input per 
 * shift register). Each bit of the returned int represents the 
 * state of one input.
 *
 * see https://www.youtube.com/watch?v=nXl4fb_LbcI to know how shift
 * register input works.
 */

class ShiftRegisteredInput
{
    public:
        ShiftRegisteredInput(ShiftRegister* sr, uint8_t firstPin, uint8_t lastPin, uint8_t inputPin);
        int read();
    private:
        uint8_t firstPin;
        uint8_t lastPin;
        ShiftRegister* sr;

        volatile uint8_t* inputPin;
        uint8_t inputBit;
};

#endif
