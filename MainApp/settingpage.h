#ifndef _SETTINGPAGE_H_
#define _SETTINGPAGE_H_

#include <QDialog>

namespace Ui {
class settingpage;
}

class settingpage : public QDialog {
    Q_OBJECT

   public:
    explicit settingpage(QWidget *parent = nullptr);
    ~settingpage();

   protected:
    virtual void mousePressEvent(QMouseEvent *event);
    virtual void mouseMoveEvent(QMouseEvent *event);
    virtual void mouseReleaseEvent(QMouseEvent *event);

   private:
    Ui::settingpage *ui;
    QPoint mMovePosition;
    bool mMoving;
};


#endif
