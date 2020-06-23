#ifndef DONATE_H
#define DONATE_H

#include <QDialog>

namespace Ui {
class donate;
}

class donate : public QDialog {
    Q_OBJECT

   public:
    explicit donate(QWidget *parent = nullptr);
    ~donate();


   protected:
    virtual void mousePressEvent(QMouseEvent *event);
    virtual void mouseMoveEvent(QMouseEvent *event);
    virtual void mouseReleaseEvent(QMouseEvent *event);

   private:
    Ui::donate *ui;
    QPoint mMovePosition;
    bool mMoving;
};

#endif // DONATE_H
