#ifndef ABOUT_H
#define ABOUT_H

#include <QDialog>

namespace Ui {
class about;
}

class about : public QDialog {
    Q_OBJECT

   public:
    explicit about(QWidget *parent = nullptr);
    ~about();


   protected:
    virtual void mousePressEvent(QMouseEvent *event);
    virtual void mouseMoveEvent(QMouseEvent *event);
    virtual void mouseReleaseEvent(QMouseEvent *event);

   private:
    Ui::about *ui;
    QPoint mMovePosition;
    bool mMoving;
};

#endif  // ABOUT_H
