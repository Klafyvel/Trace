#ifndef H_MACHINE
#define H_MACHINE

#include <math.h>

#include "Arduino.h"
#include "Servo.h"

#include "Listuino/Listuino/Listuino.h"

#include "communication.h"
#include "gcode.h"
#include "codes.h"
// #include "machineTypes.h"

class Axis
{
public:
    Axis() {}
    virtual ~Axis() {}

    virtual void move() {}
    virtual void addMovement(float value) {}
    virtual bool currentMoveFinished() const {}
    virtual uint8_t getOutput() const {return 0;}
    virtual bool isShiftRegistered() const {return false;}
    float getStepSize(){return this->stepSize;}
    float getStepTime(){return this->stepTime;}

protected:
    long lastTime;
    long stepTime;
    float stepSize;
    float remainingDistance;
    List<float> waitingMovement;
};

class ServoAxis : public Axis
{
public:
    ServoAxis(uint8_t pin, uint8_t up, uint8_t down);
    void move();
    bool currentMoveFinished() const;
    bool isShiftRegistered() const {return false;}
private:
    uint8_t up;
    uint8_t down;
    Servo servo;
};

class StepperAxis : public Axis
{
public:
    StepperAxis(long stepTime, int stepSize);
    void move();
    uint8_t getOutput() const;
    bool currentMoveFinished() const;
    bool isShiftRegistered() const {return true;}
private:
    uint8_t lastPos;
    char movementDirection;
};

class Machine
{
public:
    Machine();
    ~Machine();

    void addStepperAxis(uint8_t code, long stepTime, int stepSize); // code defined in "gcode.h"
    void addServoAxis(uint8_t code, uint8_t pin, uint8_t up, uint8_t down); // code defined in "gcode.h"
    void execute(Command command);

    void linearInterpolation(float args[]);
    void cicularInterpolationClockwise(float args[]);
    void cicularInterpolationCounterClockwise(float args[]);
private:
    Axis* axes[NB_AXIS];
    int currentSteps[NB_AXIS];
    float pos[NB_AXIS];
};


#endif
