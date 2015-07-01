#include "gcode.h"

Command parse(char* input) 
{
    if (input[0] == 'G')
        return parseG(input);
    else if (input[0] == 'M')
        return parseM(input);
    else if (input[0] == '(')
        return parseCom(input);
    else
    {
        error(strcat("Unknow command : ", input));
        Command c;
        c.num = 0;
        return c;
    }
}

Command parseM(char* input) 
{
    Command c;
    c.num = parseNum(input, 1) + 100; // See codes.h
    float *args = parseArgs(input, 1);
    for (int i=0; i<NB_ARGS; i++)
    {
      c.args[i] = args[i];
    }
    return c;
}

Command parseG(char* input) 
{
    Command c;
    c.num = parseNum(input, 1) + 1; // See codes.h 
    float *args = parseArgs(input, 1);
    for (int i=0; i<NB_ARGS; i++)
    {
      c.args[i] = args[i];
    }
    return c;
}

Command parseCom(char* input, int begin) 
{
    int i = begin;
    char c = input[i];
    while (c != '\0' && c != '\n' && c != ')') 
    {
        if (!(c == '(' && i == begin)) 
        {
            pchar(c);
        }
        i ++;
        c = input[i];
    }
}
float* parseArgs(char* input, int begin)
{
    float returned[NB_ARGS];
    char c;
    int i=begin;
    do
    {
        c = input[i];
        switch (c)
        {
            case 'X': returned[X] = parseNum(input, i); break;
            case 'Y': returned[Y] = parseNum(input, i); break;
            case 'Z': returned[Z] = parseNum(input, i); break;
            case 'I': returned[I] = parseNum(input, i); break;
            case 'J': returned[J] = parseNum(input, i); break;
            case 'F': returned[F] = parseNum(input, i); break;
            default: break;
        }
        i++;
    }while (c!='\n' && c!='\0' && (c != '('));
    return returned;
}

float parseNum(char* input, int begin)
{
    int i = begin;

    char c = input[i];
    float result = 0.0;
    bool addDecimals = false;
    bool addNegatives = false;
    int decimalLevel =10;
    float intLevel = 0.1;
    while((i < begin + 15) && (c != ' ') && (c != '\n') && (c != '\0') && (c != '('))
    {
        if(c == '.')
            i = begin + 16;
        else
            intLevel *= 10;
        i++;
        c = input[i];
    }
    i = begin;
    c = input[i];
    while((i < begin + 15) && (c != ' ') && (c != '\n') && (c != '\0') && (c != '('))
    {
        float toAdd = 0;
        if (c == '-')
            addNegatives = true;
        else if (c == '.')
        {
            addDecimals = true;
            i++;
            c = input[i];
        }
        switch(c)
        {
            case '0': toAdd = 0; break;
            case '1': toAdd = 1; break;
            case '2': toAdd = 2; break;
            case '3': toAdd = 3; break;
            case '4': toAdd = 4; break;
            case '5': toAdd = 5; break;
            case '6': toAdd = 6; break;
            case '7': toAdd = 7; break;
            case '8': toAdd = 8; break;
            case '9': toAdd = 9; break;
            default: break;       
        }
        if (addDecimals)
        {
            toAdd /= decimalLevel;
            decimalLevel *= 10;
        }
        else
        {
            toAdd *= intLevel;
            intLevel /= 10;
        }

        if (addNegatives)
            result -= toAdd;
        else
            result += toAdd;
        i++;
        c = input[i];
    }
    return result;
}
