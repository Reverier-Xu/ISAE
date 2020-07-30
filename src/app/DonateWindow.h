#ifndef DONATE_H
#define DONATE_H

#include <QDialog>

QT_BEGIN_NAMESPACE
namespace Ui {
class DonateWindow;
}
QT_END_NAMESPACE

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
