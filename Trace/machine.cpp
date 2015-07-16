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

UnipolarAxe::UnipolarAxe(long stepTime, int stepSize)
{
    this->lastTime = millis();
    this->stepTime = stepTime;
    this->stepSize = stepSize;
    this->remainingDistance = 0;
}
void UnipolarAxe::move(float value)
{
    if(value == 0 && this->remainingDistance == 0)
        return;
    else if(this->remainingDistance == 0) 
    {
        this->remainingDistance = value;
        this->lastPos = 1;
        this->lastTime = millis();
    }
    if(millis() - this->lastTime >= this->stepTime){
        this->remainingDistance -= this->stepSize;
        this->lastPos = (this->lastPos * 2) % 16 + (this->lastPos == 8); // Challenge ! find something uglier !
        this->lastTime = millis();
    }
}
uint8_t UnipolarAxe::getOutput()
{
    return this->lastPos;
}
bool UnipolarAxe::currentMoveFinished() const
{
    if (this->remainingDistance <= 0)
        return true;
    else
        return false;
}
