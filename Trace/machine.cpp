#include "machine.h"

#define SQUARE(A) A*A

Machine::Machine()
{
    for (int i = 0; i < NB_AXIS; ++i)
    {
        this->axes[i] = 0;
        this->pos[i] = 0;
        this->currentSteps[i] = 0;
    }
}
Machine::~Machine()
{
    for (int i = 0; i < NB_AXIS; ++i)
        delete this->axes[i];
}

void Machine::addStepperAxis(uint8_t code, long stepTime, int stepSize)
{
    if (this->axes[code] != 0)
        delete this->axes[code];
    this->axes[code] = new StepperAxis(stepTime, stepSize);
}

void Machine::addServoAxis(uint8_t code, uint8_t pin, uint8_t up, uint8_t down)
{
    if (this->axes[code] != 0)
        delete this->axes[code];
    this->axes[code] = new ServoAxis(pin, up, down);
}

void Machine::execute(Command command)
{
    bool move = false;
    switch (command.num)
    {
        case G00:case G01: this->linearInterpolation(command.args);move=true;break;
        default: break;
    }
    if (move)
    {
        for (int i = 0; i < NB_AXIS; ++i)
        {
            for (int j = 0; j < this->currentSteps[i]; ++j)
            {
                this->axes[j]->move();
                delay(this->axes[j]->getStepTime());
            }
        }
    }
}

void Machine::linearInterpolation(float args[]) 
{
    for (int i = 0; i < NB_AXIS; ++i)
    {
        this->currentSteps[i] = abs(args[i] - this->pos[i]) / this->axes[i]->getStepSize();
        this->axes[i]->addMovement(args[i]);
        this->pos[i] = args[i];
    }
}

void Machine::cicularInterpolationClockwise(float args[])
{
    float radius = sqrt(args[I]*args[I] + args[J]*args[J] + args[K]*args[K]);
    for (int i = 0; i < NB_AXIS; ++i)
    {
        this->currentSteps[i] = acos(this->axes[i]->getStepSize()/radius);
    }
}
void Machine::cicularInterpolationCounterClockwise(float args[])
{
    float radius = sqrt(args[I]*args[I] + args[J]*args[J]);
    float arc = 2 * PI * radius;
    float stepArc = sqrt(SQUARE(this->axes[X]->getStepSize()) + SQUARE(this->axes[Y]->getStepSize()));
    for (int i = 0; i < (arc / stepArc); ++i)
    {
        this->axes[X]->addMovement(cos(i)*radius);
        this->axes[Y]->addMovement(-sin(i)*radius);
    }

}

ServoAxis::ServoAxis(uint8_t pin, uint8_t up, uint8_t down)
{
    this->up = up;
    this->down = down;
    this->servo.attach(pin);
}

void ServoAxis::move()
{
    if (this->waitingMovement.getLength() <= 0)
        return;
    float value = this->waitingMovement.popFirst();
    if (value >= 0)
        this->servo.write(this->up);
    else
        this->servo.write(this->down);
}

StepperAxis::StepperAxis(long stepTime, int stepSize)
{
    this->lastTime = millis();
    this->stepTime = stepTime;
    this->stepSize = stepSize;
    this->remainingDistance = 0;
    this->lastPos = 1;
}
void StepperAxis::move()
{
    if(this->remainingDistance <= 0 && this->waitingMovement.getLength() > 0) 
    {
        this->remainingDistance = this->waitingMovement.popFirst();
        this->lastTime = millis();
        this->movementDirection = this->remainingDistance / abs(this->remainingDistance);
    }
    else if(millis() - this->lastTime >= this->stepTime){
        this->remainingDistance += this->stepSize * this->movementDirection;
        this->lastPos = (this->lastPos * 2) % 16 + (this->lastPos == 8);
        this->lastTime = millis();
    }
}
uint8_t StepperAxis::getOutput() const
{
    return this->lastPos;
}
bool StepperAxis::currentMoveFinished() const
{
    return (this->remainingDistance <= 0);
}
