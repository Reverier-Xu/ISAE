//
// Created by reverier on 2020/7/9.
//

#ifndef ISAE_MAINAPPSETTINGPAGE_H
#define ISAE_MAINAPPSETTINGPAGE_H

#include <QWidget>
#include <QSettings>
#include <QSaveFile>
namespace Ui {
    class MainAppSettingPage;
}

class MainAppSettingPage : public QWidget {
    Q_OBJECT
private:
    QSettings* m_settings;
    bool m_isValid = false;
    Ui::MainAppSettingPage *ui;
public:
    explicit MainAppSettingPage(QWidget *parent = nullptr);
    ~MainAppSettingPage() override;
public slots:
    void saveSetting();
    void loadSetting(const QString& path);
    bool isValid() const;
    void drawSetting();
    const QSettings& setting();
};


#endif //ISAE_MAINAPPSETTINGPAGE_H
