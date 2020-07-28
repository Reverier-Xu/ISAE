//
// Created by reverier on 2020/7/18.
//

#ifndef ISAE_ISAEPLUGINWIDGET_H
#define ISAE_ISAEPLUGINWIDGET_H

#include <QWidget>
#include <QMainWindow>
#include <QtCore>

class ISAEPluginSettingWidget;

class ISAEPluginWidget : public QMainWindow {
Q_OBJECT
    Q_PROPERTY(QString pluginName READ pluginName WRITE setPluginName)
    Q_PROPERTY(QSettings *settings READ settings WRITE setSettings)
    Q_PROPERTY(ISAEPluginSettingWidget *settingWindow READ settingWindow WRITE setSettingWindow)
protected:
    QString m_name;
    QList<QString> m_dependents;
    QList<ISAEPluginWidget *> m_listener_list;
    QSettings *m_settings {};
    ISAEPluginSettingWidget *m_settingWindow {};
public:
    explicit ISAEPluginWidget(QWidget *parent = nullptr, QFlags<Qt::WindowType> flags = Qt::WindowFlags())
            : QMainWindow(parent, flags) { };

    virtual bool registerListener(ISAEPluginWidget *listener) {
        if (this->m_listener_list.count(listener) == 0) {
            this->m_listener_list.push_back(listener);
            return true;
        }
        return false;
    };

    virtual bool removeListener(ISAEPluginWidget *listener) {
        return this->m_listener_list.removeOne(listener);
    };

    virtual bool setSettings(QSettings *s) {
        this->m_settings = s;
        return true;
    };

    virtual QSettings *settings() { return this->m_settings; };

    virtual ISAEPluginSettingWidget *settingWindow() { return this->m_settingWindow; };

    virtual bool setSettingWindow(ISAEPluginSettingWidget *settingWidget) {
        this->m_settingWindow = settingWidget;
        return true;
    };

    // 插件名称的设置与获取
    void setPluginName(const QString &name) { this->m_name = name; };

    QString pluginName() { return this->m_name; };

    // 广播函数
    bool notify(const QVector<QString> &info) {
        bool ok = true;
        for (auto &i : this->m_listener_list) {
            ok = i->updateStatus(info);
        }
        return ok;
    };
    // 接收函数, 由用户自行实现
    virtual bool updateStatus(QVector<QString> info) = 0;
    // 应用设置, 由用户自行实现
    virtual bool applySettings() = 0;
};


class ISAEPluginSettingWidget : public QWidget {
Q_OBJECT
protected:
    QSettings *m_settings{};
    ISAEPluginWidget *m_pluginWidget{};
public:
    explicit ISAEPluginSettingWidget(QWidget* parent):QWidget(parent){};
    void applySettings() {
        this->m_pluginWidget->applySettings();
    }
    // 加载设置文件, 由用户自行实现
    virtual bool loadSettings(const QString &path) = 0;

    virtual bool saveSettings() = 0;

    QSettings *setting() {
        return this->m_settings;
    }
};

#endif //ISAE_ISAEPLUGINWIDGET_H
