#include <QMenu>
#include "menubutton.h"
#include<QRect>
MenuButton::MenuButton(QWidget *parent) :
    QToolButton(parent)
{
    menu = new QMenu(this);

    connect(this,SIGNAL(clicked()),this,SLOT(popupmenu()));//点击按钮就弹出菜单
}

QMenu *MenuButton::getmenu()
{
     return menu;
}

void MenuButton::popupmenu()
{
     QPoint pos; //获取按键菜单的坐标

    // int x = pos.x();

     int y = pos.y();
    // pos.setX(x + this->geometry().width()/2);//也可以改变出现菜单的窗口的x位置

     pos.setY(y + 32);
    menu->exec(this->mapToGlobal(pos));

}
