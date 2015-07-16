#include <Wire.h>

#include "LiquidCrystal.h"
#include "Servo.h"

#include "menu.h"
#include "settings.h"
#include "communication.h"
#include "gcode.h"
#include "machine.h"

LiquidCrystal lcd(11,10,5,4,3,2);


const uint8_t BP_UP = 6;
const uint8_t BP_DOWN = 7;
const uint8_t BP_OK = 8;

const uint8_t SERVO_PIN = 9;

Menu myMenu("Menu principal", &lcd, BP_UP, BP_DOWN, BP_OK);

Servo servo;

uint8_t servoHaut = 90;
uint8_t servoBas = 90;

void setup()
{
    Serial.begin(9600);
    lcd.begin(16, 2);

    servo.attach(SERVO_PIN);
    servo.write(servoHaut);

    myMenu.addItem(&reglageServo, "Reglage du servo");
    myMenu.addItem(&testServo, "Test du servo");
    myMenu.addItem(&testGCode, "Test gcode");
    myMenu.addItem(&testUnipolar, "Test unipolaire");
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
    parse("G01 Z-1.000000 F100.0(Penetrate)");
}
void testUnipolar()
{
    lcd.clear();
    lcd.print("Test axe unipolaire");
    Axe axe = UnipolarAxe(20, 1);
    axe.move(42);
    while(!axe.currentMoveFinished())
    {
        uint8_t o = axe.getOutput();
        axe.move();
        dvar(o);
    }
}
