#ifndef _SETTINGPAGE_H_
#define _SETTINGPAGE_H_

#include <QDialog>
#include <QSettings>
#include <QListWidgetItem>

namespace Ui {
class SettingWindow;
}

class SettingWindow : public QDialog {
    Q_OBJECT

   public:
    explicit SettingWindow(QWidget *parent = nullptr);
    ~SettingWindow();

   protected:
    virtual void mousePressEvent(QMouseEvent *event);
    virtual void mouseMoveEvent(QMouseEvent *event);
    virtual void mouseReleaseEvent(QMouseEvent *event);

   private:
    Ui::SettingWindow *ui;
    QPoint mMovePosition;
    bool mMoving;
};


#endif
