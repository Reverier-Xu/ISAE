#include "menubutton.h"

#include <QMenu>
#include <QRect>

MenuButton::MenuButton(QWidget *parent) : QToolButton(parent) {
    menu = new QMenu(this);

    connect(this, SIGNAL(clicked()), this,
            SLOT(popupmenu()));  //点击按钮就弹出菜单
}

QMenu *MenuButton::getmenu() { return menu; }

void MenuButton::popupmenu() {
    QPoint pos;  //获取按键菜单的坐标

    int y = pos.y();

    pos.setY(y + 32);
    menu->exec(this->mapToGlobal(pos));
}
