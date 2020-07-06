#ifndef DONATE_H
#define DONATE_H

#include <QDialog>

namespace Ui {
class DonateWindow;
}

class DonateWindow : public QDialog {
    Q_OBJECT

   public:
    explicit DonateWindow(QWidget *parent = nullptr);
    ~DonateWindow() override;

   protected:
    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;

   private:
    Ui::DonateWindow *ui;
    QPoint mMovePosition;
    bool mMoving;
};

#endif  // DONATE_H
