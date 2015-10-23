#include "LiquidCrystal.h"
#include "Servo.h"

#include "menu.h"
#include "settings.h"
#include "communication.h"
#include "gcode.h"
#include "machine.h"
#include "ShiftRegister/shiftRegister.h"
#include "shiftRegisteredInput.h"

#include "ShiftRegister/shiftRegister.cpp"

LiquidCrystal lcd(13,12,11,10,9,8);

#define BP_UP 1
#define BP_DOWN 0
#define BP_OK 2

#define SHCP 6
#define STCP 5
#define DS 4

#define SERVO_PIN 9

Servo servo;

ShiftRegister sr(SHCP,STCP,DS);

ShiftRegisteredInput sri(&sr, 8, 16, 2);

Menu myMenu("Menu principal", &lcd, &sri, BP_UP, BP_DOWN, BP_OK);

Machine machine = Machine();

uint8_t servoHaut = 90;
uint8_t servoBas = 90;

void setup()
{
    Serial.begin(9600);
    lcd.begin(16, 2);
    lcd.print("Bienvenue");
    uint8_t test[] = {0xFF, 0xFF};
    sr.sendBytes(test, 2);
    test[0] = 0;
    test[1] = 0;
    delay(15000);
    //sr.sendBytes(test, 2);

    servo.attach(SERVO_PIN);
    servo.write(servoHaut);

    myMenu.addItem(&reglageServo, "Reglage du servo");
    myMenu.addItem(&testServo, "Test du servo");
    myMenu.addItem(&testGCode, "Test gcode");
    myMenu.addItem(&testUnipolar, "Test unipolaire");

    machine.addStepperAxis(X, 20, 1);
    machine.addStepperAxis(Y, 20, 1);
    machine.addServoAxis(Z, 2, 80, 100);

}
void loop()
{
    int action = myMenu.choose();
    if(action != -1)
    {
        myMenu.action(action);
    }

}
void reglageServo()
{
    Menu menuReglage("Reglage du servo", &lcd, BP_UP, BP_DOWN, BP_OK);
    menuReglage.addItem(&reglageServoHaut, "Position haute");
    menuReglage.addItem(&reglageServoBas, "Position basse");
    int action = menuReglage.choose();
    if(action != -1)
    {
        menuReglage.action(action);
    }

}
void reglageServoHaut()
{
    lcd.clear();
    lcd.print("Regl. servo haut");
    lcd.setCursor(0,1);
    lcd.print("Enregistrer : OK");
    uint8_t val = servoHaut;
    while(digitalRead(BP_OK)){
        val = (float)(analogRead(0))/1023.0*180.0;
        servo.write(val);
        dvar(val);
    }
    servoHaut = val;
    servo.write(servoHaut);
}

void reglageServoBas()
{
    lcd.clear();
    lcd.print("Regl. servo bas");
    lcd.setCursor(0,1);
    lcd.print("Enregistrer : OK");
    uint8_t val = servoBas;
    while(digitalRead(BP_OK)){
        val = (float)(analogRead(0))/1023.0*180.0;
        servo.write(val);
    }
    servoBas = val;
    servo.write(servoHaut);
}

void testServo()
{
    lcd.clear();
    lcd.print("Test du servo");
    for(int i=0; i<10000; i++){
        servo.write(servoHaut);
        delay(10);
        servo.write(servoBas);
        delay(10);
    }
    servo.write(servoHaut);
}

void testGCode()
{
    lcd.clear();
    lcd.print("Test du gcode...");
    Command cmd = parse("G01 Z-1.000000 F100.0(Penetrate)");
    dvar(cmd.num);
    for(int i=0; i<NB_ARGS; i++){
        dvar(cmd.args[i]);
    }

}
void testUnipolar()
{
    lcd.clear();
    lcd.print("Test axe unipolaire");
    StepperAxis axe = StepperAxis(20, 5);
    // axe.move(42);
    while(!axe.currentMoveFinished())
    {
        uint8_t o = axe.getOutput() << 4;
        axe.move();
        uint8_t toSend[] = {o,0}; // sweet smiley
        sr.sendBytes(toSend, 2); 
    }
}
