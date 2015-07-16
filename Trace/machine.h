#ifndef H_MACHINE
#define H_MACHINE

#include "Arduino.h"

#include "Servo.h"

#include "communication.h"

#include "gcode.h"

class Axe
{
public:
    Axe() {};
    virtual ~Axe() {};

    virtual void move(float value=0) {};
    virtual bool currentMoveFinished() const {};
    
    virtual uint8_t getOutput() {};

    bool isShiftRegistered;

protected:
    long lastTime;
    long stepTime;
    int stepSize;
    int remainingDistance;
};

class Machine
{
public:
    Machine();
    ~Machine();

    void addAxe(uint8_t code, Axe axe); // code defined in "gcode.h"

private:
    Axe axes[NB_AXES];    
};

class ServoAxe : public Axe
{
public:
    ServoAxe(uint8_t pin, uint8_t up, uint8_t down);
   void move(float value);
    bool currentMoveFinished() const;
    const bool isShiftRegistered = false;
private:
    uint8_t up;
    uint8_t down;
    Servo servo;
};

class StepperAxe : public Axe
{
public:
    StepperAxe(long stepTime, int stepSize);
    void move(float value=0);
    uint8_t getOutput();
    bool currentMoveFinished() const;
    const bool isShiftRegistered = true;
private:
    uint8_t lastPos;
};

#endif
