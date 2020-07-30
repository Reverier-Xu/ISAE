//
// Created by reverier on 2020/7/9.
//

#ifndef ISAE_MAINAPPSETTINGPAGE_H
#define ISAE_MAINAPPSETTINGPAGE_H

#include <QWidget>
#include <QSettings>
#include <QSaveFile>
#include "ISAEPluginWidget.h"

namespace Ui {
    class MainAppSettingPage;
}

class MainAppSettingPage : public ISAEPluginSettingWidget {
Q_OBJECT
private:
    Ui::MainAppSettingPage *ui;
public:
    explicit MainAppSettingPage(QWidget *parent);

    ~MainAppSettingPage() override;

    void drawSettings();

    bool loadSettings(const QString &path) override;

    bool saveSettings() override;
};


#endif //ISAE_MAINAPPSETTINGPAGE_H
