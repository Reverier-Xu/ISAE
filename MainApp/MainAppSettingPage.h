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
    explicit MainAppSettingPage(QWidget *parent = nullptr);
    ~MainAppSettingPage() override;
    bool isValid() const;
    void drawSetting();
    QSettings* setting();
public slots:
    void saveSetting() override;
    void loadSetting(const QString& path) override;
};


#endif //ISAE_MAINAPPSETTINGPAGE_H
