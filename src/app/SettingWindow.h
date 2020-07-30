#ifndef _SETTINGPAGE_H_
#define _SETTINGPAGE_H_

#include <QDialog>
#include <QSettings>
#include <QListWidgetItem>
#include "ISAEPluginWidget.h"

QT_BEGIN_NAMESPACE
namespace Ui {
    class SettingWindow;
}
QT_END_NAMESPACE

class SettingWindow : public QDialog {
Q_OBJECT

public:
    explicit SettingWindow(QWidget *parent = nullptr);

    ~SettingWindow() override;

    void addPage(const QString &name, ISAEPluginSettingWidget *page, ISAEPluginWidget *Plugin);

    void clearPages();

public slots:

    void changePage(QListWidgetItem *item);

    void applySettings();

    void saveSettings();

protected:
    void mousePressEvent(QMouseEvent *event) override;

    void mouseMoveEvent(QMouseEvent *event) override;

    void mouseReleaseEvent(QMouseEvent *event) override;

private:
    Ui::SettingWindow *ui;
    QPoint mMovePosition;
    bool mMoving;
    QMap<QString, ISAEPluginSettingWidget *> settingPageMap {};
    QMap<QString, ISAEPluginWidget *> pluginMap {};
};


#endif
