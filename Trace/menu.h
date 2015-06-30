#ifndef H_MENU
#define H_MENU

#include "Arduino.h"
#include "LiquidCrystal.h"

#include <string.h>

#define MAX_ITEM 10
#define MAX_LABEL_LONG 20

typedef void (*callback)(void);
class Menu;

typedef struct Item
{
    Item* suivant;
    Menu* sousMenu;
    callback fonction;
    char label[MAX_LABEL_LONG];
} Item;

int Menu_newItem(Item* item, callback fonction, const char nom[]);
int Menu_newItemSubMenu(Item* item, Menu* subMenu, const char nom[]);
// int Menu_setSubMenu(Item* item, Menu* subMenu);

class Menu
{
public:
    Menu(char titre[], LiquidCrystal* lcd, \
         char bp_haut, char bp_bas, char bp_ok);
    ~Menu();
    int addSubMenu(Menu* submenu, const char nom[]);
    int addItem(callback fonction, const char nom[]);
    int addItem(Item* item);
    int removeItemByLabel(const char nom[]);
    int removeItemById(int id);
    int action(int action);
    int choose();
    void print(char current);

private:
    int nombreItem;
    Item* premier;
    char titre[MAX_LABEL_LONG];
    LiquidCrystal* lcd;
    char bp_haut;
    char bp_bas;
    char bp_ok;
    int last_item;
};
#endif