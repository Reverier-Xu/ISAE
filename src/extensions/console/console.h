//
// Created by reverier on 2020/8/14.
//

#ifndef ISAE_CONSOLE_H
#define ISAE_CONSOLE_H

#include <QWidget>
#include <ISAEPluginWidget.h>
#include <QVBoxLayout>
#include <QDebug>
#include "qtermwidget.h"

class ConsoleSettingPage : public ISAEPluginSettingWidget {
Q_OBJECT
public:
    explicit ConsoleSettingPage(QWidget *parent = nullptr) : ISAEPluginSettingWidget(parent) { };

    ~ConsoleSettingPage() override = default;

    bool loadSettings(const QString &path) override { return true; };

    bool saveSettings() override { return false; };

};

class Console : public ISAEPluginWidget {
Q_OBJECT
public:
    explicit Console(QWidget *parent = nullptr, QFlags<Qt::WindowType> flags = Qt::WindowFlags())
            : ISAEPluginWidget(parent, flags) {
        this->m_name = "Console";
        this->m_icon = ":/plugins/console.svg";
        QTermWidget *console = new QTermWidget();
        this->setCentralWidget(console);
        this->m_settingWindow = new ConsoleSettingPage(this);
    };

    ~Console() override = default;

    // 接收函数, 由用户自行实现
    bool updateStatus(QVector<QString> info) override { return true; };

    // 应用设置, 由用户自行实现
    bool applySettings() override { return true; };
};


#endif //ISAE_CONSOLE_H
