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
    ~SettingWindow() override;
    void addPage(const QString& name, QWidget *page);

public slots:
    void changePage(QListWidgetItem* item);

   protected:
    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;

   private:
    Ui::SettingWindow *ui;
    QPoint mMovePosition;
    bool mMoving;
    QMap<QListWidgetItem*, QWidget*> map{};
};


#endif
