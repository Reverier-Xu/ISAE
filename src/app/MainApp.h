//
// Created by reverier on 2020/7/13.
//

#ifndef ISAE_MAINAPP_H
#define ISAE_MAINAPP_H

#include <QMainWindow>
#include "ISAEPluginWidget.h"
#include <QPushButton>
#include "MainAppSettingPage.h"
#include "SettingWindow.h"
#include "AboutWindow.h"
#include "DonateWindow.h"
#include <DockManager.h>

QT_BEGIN_NAMESPACE
namespace Ui {
    class MainApp;
}
QT_END_NAMESPACE

class MainApp : public ISAEPluginWidget {
Q_OBJECT
private:
    Ui::MainApp *ui;
    // 状态栏组件
    QPushButton *WootecStatusBox {};
    QPushButton *CPUStatusBox {};
    QPushButton *agileEngineBox {};
    // 默认字体
    QFont m_defaultFont {};
    // 标识窗口是否在移动
    bool m_isMoving {false};
    // 窗口移动变量
    QPoint m_MovePosition;
    // 标识用户区是否展开. 此项和侧边栏展开一同变化
    bool m_isClientFold {false};
    // 设置对话框
    SettingWindow *m_settingDialog {};
    // 用户信息
    QString m_clientName {};
    QIcon m_clientIcon {};
    // 关于窗口与捐助窗口
    AboutWindow *m_aboutWindow {};
    DonateWindow *m_donateWindow {};
    QMap<QString, ads::CDockWidget *> m_plugins {};

    // 设置状态栏
    void setStatusBarButton();

    // 返回用户区是否折叠
    [[nodiscard]] bool isClientFold() const;

    // 设置用户区折叠状态
    void setClientFold(bool flag);


protected:
    /* 窗口事件 */
    void mousePressEvent(QMouseEvent *event) override;

    void mouseMoveEvent(QMouseEvent *event) override;

    void mouseReleaseEvent(QMouseEvent *event) override;

public slots:

    /* 窗口调整 */
    void changeWindowStatus();

    void doFoldClient();

/* 显示关于页 */
    void showAboutWindow() { this->m_aboutWindow->show(); }

    void showDonateWindow() { this->m_donateWindow->show(); }

    void showSettingWindow() { this->m_settingDialog->show(); }

    void showAppDock(const QString &plugin);

public:
    // 构造函数
    explicit MainApp(QWidget *parent = nullptr, QFlags<Qt::WindowType> flags = Qt::WindowFlags());

    ~MainApp() override = default;

    // 重载的状态更新选项
    bool updateStatus(QVector<QString> info) override { return true; };

    // 重载的设置更新选项
    bool applySettings() override;

    // 应用样式表
    void loadStyleSheet(const QString &styleSheetFile);

    // 探测应用目录
    static void detectDirs();

    // 更新用户信息
    [[maybe_unused]] void showClient(QString name, QIcon icon);

    // 设置背景
    void setBackground(const QImage &image, int blur);

    // 设置所有插件
    void getPlugins();

    // 设置各个插件的设置页面
    void setPluginSettingWindow();

    // 设置外部窗口, 包括捐助页面, 关于页面, 设置窗口
    void setExtendWindow();

    void addPlugin(ISAEPluginWidget *plugin);

    void addPluginButton(QPushButton *button);

};

#endif //ISAE_MAINAPP_H
