#ifndef MENUBUTTON_H
#define MENUBUTTON_H


#include <QToolButton>
#include <QMenu>

class MenuButton : public QToolButton
{
    Q_OBJECT
public:
    explicit MenuButton(QWidget *parent = nullptr);
    QMenu * getmenu();
    QMenu * menu;
signals:

public slots:
    void popupmenu();
};

#endif // MENUBUTTON_H
