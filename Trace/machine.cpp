#include "machine.h"

Machine::Machine()
{

}

void Machine::addAxe(uint8_t code, Axe axe)
{
    this->axes[code] = axe;
}

ServoAxe::ServoAxe(uint8_t pin, uint8_t up, uint8_t down)
{
    this->up = up;
    this->down = down;
    this->servo.attach(pin);
}

void ServoAxe::move(float value)
{
    if (value >= 0)
        this->servo.write(this->up);
    else
        this->servo.write(this->down);
}

