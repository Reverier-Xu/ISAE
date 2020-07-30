//
// Created by reverier on 2020/7/29.
//

#ifndef ISAE_FILEMANAGERSETTINGPAGE_H
#define ISAE_FILEMANAGERSETTINGPAGE_H

#include "ISAEPluginWidget.h"

QT_BEGIN_NAMESPACE
namespace Ui {
    class FileManagerSettingPage;
}
QT_END_NAMESPACE

class FileManagerSettingPage : public ISAEPluginSettingWidget {
Q_OBJECT
public:
    explicit FileManagerSettingPage(QWidget *parent = nullptr);

    bool loadSettings(const QString &path) override { return true; };

    bool saveSettings() override { return false; };

private:
    Ui::FileManagerSettingPage *ui;

};


#endif //ISAE_FILEMANAGERSETTINGPAGE_H
