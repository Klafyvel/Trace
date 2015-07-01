#ifndef H_MACHINE
#define H_MACHINE

#include "Arduino.h"

#include "Servo.h"

#include "communication.h"

class Machine
{
public:
    Machine();
    ~Machine();

    void addServoAxe(char name, ServoAxe axe);
    void addUnipolarAxe(char name, UnipolarAxe axe);
    void addBipolarAxe(char name, BipolarAxe axe);

    void removeAllAxes();

private:
    Axe axes[NB_AXES];    
};

class Axe
{
public:
    Axe();
    ~Axe();

    virtual void move(float value);
    bool isShiftRegistered;

protected:
    long lastTime;
    long stepTime;

};

class ServoAxe : public Axe
{
public:
    ServoAxe(uint8_t pin, uint8_t up, uint8_t down);
    void move(float value);
    bool isShiftRegistered = false;
private:
    uint8_t up;
    uint8_t down;
    Servo servo;
};

class UnipolarAxe : public Axe
{
public:
    UnipolarAxe(uint8_t pin);
    void move(float value);
    bool isShiftRegistered = true;  
private:
    uint8_t lastPos;
};

class BipolarAxe : public Axe
{
public:
    BipolarAxe(uint8_t pin);
    void move(float value);
    bool isShiftRegistered = true;  
private:
    uint8_t lastPos;
};

#endif
