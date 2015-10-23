#include "menu.h"

Menu::Menu(char titre[], LiquidCrystal* lcd, char bp_haut, char bp_bas, char bp_ok)
{
    this->nombreItem = 0; 
    this->premier = NULL; 
    this->lcd = lcd;
    this->lcd->noBlink();
    this->lcd->noCursor();
    this->bp_ok = bp_ok;
    this->bp_haut = bp_haut;
    this->bp_bas = bp_bas;
    this->last_item = 0;
    this->isShiftRegistered = false;

    pinMode(bp_ok, INPUT);
    pinMode(bp_haut, INPUT);
    pinMode(bp_bas, INPUT);
    digitalWrite(bp_ok, HIGH);
    digitalWrite(bp_haut, HIGH);
    digitalWrite(bp_bas, HIGH);

    if(strlen(titre) <= 100){strcpy(this->titre, titre);}
}
Menu::Menu(char titre[], LiquidCrystal* lcd, ShiftRegisteredInput* sri, uint8_t bp_haut, uint8_t bp_bas, uint8_t bp_ok)
{
    this->nombreItem = 0; 
    this->premier = NULL; 
    this->lcd = lcd;
    this->lcd->noBlink();
    this->lcd->noCursor();
    this->last_item = 0;
    this->bp_ok = bp_ok;
    this->bp_haut = bp_haut;
    this->bp_bas = bp_bas;

    this->isShiftRegistered = true;
    this->sri = sri;

    if(strlen(titre) <= 100){strcpy(this->titre, titre);}
}
int Menu::addItem(callback fonction, const char nom[])
{
    Item* item = new Item;
    return item!= NULL && Menu_newItem(item, fonction, nom) && Menu::addItem(item);
}
int Menu::addSubMenu(Menu* submenu, const char nom[])
{
    Item* item = new Item;
    return item!= NULL && Menu_newItemSubMenu(item, submenu, nom) && Menu::addItem(item);
}
int Menu::addItem(Item* item) 
{
    if(this->nombreItem==0){this->premier = item;}
    else
    {
        Item* buffer = NULL;
        buffer=this->premier;
        if(buffer == NULL)
            return 0;
        while(buffer->suivant){buffer = buffer->suivant;}
        buffer->suivant = item;
    }
    this->nombreItem ++;

    return 1;
}

int Menu::removeItemByLabel(const char nom[])
{
    Item* item = this->premier;
    while(strcmp(item->suivant->label, nom)) 
    {
        item = item->suivant;
    }
    delete item->suivant;
    item->suivant = item->suivant->suivant; 
    this->nombreItem --; 
    return 1;
}

int Menu::removeItemById(int id) 
{
    if((id < 0)||(id >= this->nombreItem)) 
    {
        return 0; 
    }
    else 
    {

        int i; 
       Item* item = this->premier; 
        for(i = 1; i<id; i++) 
        {
            item = item->suivant;
        }
        delete item->suivant;
        item->suivant = item->suivant->suivant; 
        this->nombreItem --; 
    }
    return 1;
}

Menu::~Menu() 
{
    Item* buffer = this->premier;
    do
    {
        this->premier = buffer->suivant;
        delete buffer;
        buffer = this->premier;
    }while(buffer != NULL);
}
void Menu::print(char current)
{
    this->lcd->clear();
    this->lcd->print(this->titre);
    this->lcd->print(" :");
    int i= 0;
    Item* item = this->premier;
    this->lcd->setCursor(0,1);
    if(current<this->nombreItem) {
        for(i=0; i<current; i++)
            item = item->suivant;
        this->lcd->print(item->label);
    }
    else {
        this->lcd->print("Quitter");
    }
}

int Menu::choose() 
{
    unsigned int choix = this->nombreItem+1; 
    int current = this->last_item;
    while((choix < 0) || (choix > this->nombreItem))
    {
        bool event = false;
        Menu::print(current);
        while(!event) {
            if(this->isShiftRegistered)
            {
               int input = this->sri->read();
               dvar(input);
               if(input&(1<<this->bp_bas)) {current ++;event=true;}
               if(input&(1<<this->bp_haut)) {current --;event=true;}
               if(input&(1<<this->bp_ok)) {choix = current;event=true;}
            }
            else {
                if(digitalRead(this->bp_bas)==LOW) { current ++;event = true;}
                if(digitalRead(this->bp_haut)==LOW) { current --;event = true;}
                if(digitalRead(this->bp_ok)==LOW) { choix = current;event = true;}
            }
            current = (this->nombreItem + 1 + current)%(this->nombreItem+1);
        }
        delay(200);
    }
    if(choix==this->nombreItem) 
    {
        this->last_item = 0;
        return -1;
    }
    else
    {
        this->last_item = choix;
        return choix;
    }
}

int Menu::action(int action)
{
    if((action<0)||(action >= this->nombreItem))
    {
        return 0;
    }
    else
    {
        callback fonction;
       int i;
       Item* item = this->premier;
       for(i=0; i<action; i++)
       {
           item = item->suivant;
       }
       if(item->fonction)
       {
            fonction = item->fonction;
            fonction();
        }
        else if(item->sousMenu)
        {
            int a;
            do {
                a = item->sousMenu->choose();
                item->sousMenu->action(a);
            }while(a>=0);
        }
    }
    return 1;
}

int Menu_newItem(Item* item, callback fonction, const char nom[])
{
    item->fonction = fonction;
    strcpy(item->label, nom);
    item->suivant=NULL;
    item->sousMenu=NULL;

    return 1;
}
int Menu_newItemSubMenu(Item* item, Menu* subMenu, const char nom[])
{
    item->fonction = NULL;
    item->sousMenu = subMenu;
    strcpy(item->label, nom);
    item->suivant = NULL;
    return 1;
}


