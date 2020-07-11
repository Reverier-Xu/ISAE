//
// Created by reverier on 2020/7/10.
//

#ifndef ISAE_ISAEPLUGINWIDGET_H
#define ISAE_ISAEPLUGINWIDGET_H

#include <QObject>
#include <QSettings>
#include <QMainWindow>
#include <QWidget>
#include <QObject>

class ISAEPluginWidget : public QMainWindow {
Q_OBJECT
protected:
    QSettings *m_settings {};
public:
    explicit ISAEPluginWidget(QWidget *parent = nullptr,
            Qt::WindowFlags flags = Qt::WindowFlags()) : QMainWindow(parent, flags) { }
    virtual void applySetting() = 0;
};

class ISAEPluginSettingWidget : public QWidget {
Q_OBJECT
protected:
    QSettings *m_settings {};
    bool m_isValid = false;
public:
    explicit ISAEPluginSettingWidget(QWidget *parent = nullptr, Qt::WindowFlags f = Qt::WindowFlags()):
    QWidget(parent, f){}
    virtual void saveSetting() = 0;
    virtual void loadSetting(const QString &path) = 0;
};

#endif //ISAE_ISAEPLUGINWIDGET_H
