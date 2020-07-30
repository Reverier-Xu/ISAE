//
// Created by reverier on 2020/7/29.
//

#ifndef ISAE_EDITORSETTINGPAGE_H
#define ISAE_EDITORSETTINGPAGE_H

#include <QWidget>
#include "ISAEPluginWidget.h"

QT_BEGIN_NAMESPACE
namespace Ui {
    class EditorSettingPage;
}
QT_END_NAMESPACE

class EditorSettingPage : public ISAEPluginSettingWidget {
Q_OBJECT
public:
    explicit EditorSettingPage(QWidget *parent = nullptr);

    bool loadSettings(const QString &path) override { return true; };

    bool saveSettings() override { return false; };

private:
    Ui::EditorSettingPage *ui;

};


#endif //ISAE_EDITORSETTINGPAGE_H
