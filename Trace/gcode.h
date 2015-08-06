#ifndef H_GCODE
#define H_GCODE

#include "Arduino.h"

#include "communication.h"

// Axes

#define X 0
#define Y 1
#define Z 2
#define I 3
#define J 4
#define F 5

// Commands settings

#define NB_ARGS 6
#define NB_AXES 3

typedef struct Command
{
    uint8_t num;
    float args[NB_ARGS];
} Command;

Command parse(char* input);

Command parseG(char* input);
Command parseM(char* input);
Command parseCom(char* input, int begin=0);

float* parseArgs(char* input, int begin=0);

float parseNum(char* input, int begin=0);

#endif
