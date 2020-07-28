#ifndef ABOUT_H
#define ABOUT_H

#include <QDialog>

namespace Ui {
class AboutWindow;
}

class AboutWindow : public QDialog {
    Q_OBJECT

   public:
    explicit AboutWindow(QWidget *parent = nullptr);
    ~AboutWindow() override;

   protected:
    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;

   private:
    Ui::AboutWindow *ui;
    QPoint mMovePosition;
    bool mMoving;
};

#endif  // ABOUT_H
