#ifndef MAINAPP_H
#define MAINAPP_H

#include <AboutWindow.h>
#include <DonateWindow.h>
#include <SettingWindow.h>

#include <QMainWindow>
#include <QTimer>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainApp : public QMainWindow {
    Q_OBJECT

   public:
    explicit MainApp(QWidget *parent = nullptr);
    ~MainApp() override;

   public slots:
    /* 窗口调整 */
    void changeWindowStatus();

    /* 展开动画 */
    void sideBarAnimating();
    void activateSideBarAnimation();
    void appsAreaAnimating();
    void activateAppsAreaAnimation();
    void teamAreaAnimating();
    void activateTeamAreaAnimation();
    void workspaceAreaAnimating();
    void activateWorkspaceAreaAnimation();

    /* 子窗口显示 */
    void showAboutWindow();
    void showDonateWindow();
    void showSettingWindow();
    void upgradeCPUStatus();

    /* 设置背景 */
    void setBackground(const QImage& image, int blur);

    /* 侧栏添加项目 */
    void addApp(const QIcon& icon, const QString& name);
    void addWorkspace(const QIcon& icon, const QString& name);
    void addTeam(const QIcon& icon, const QString& name);
    void showClient(QString name, QIcon icon = QIcon());

   protected:
    /* 窗口事件 */
    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;

   private:
    Ui::MainWindow *ui;
    bool m_isMoving;
    QPoint m_MovePosition;
    bool m_isSidebarShow;
    bool m_isAppsAreaShow;
    bool m_isTeamAreaShow;
    bool m_isWorkspaceAreaShow;
    QTimer m_sideBarAnimation;
    QTimer m_appsAreaAnimation;
    QTimer m_teamAreaAnimation;
    QTimer m_workspaceAreaAnimation;
    QTimer m_CPUMonitorTimer;
    int m_startDuration;
    AboutWindow *aboutWindow;
    DonateWindow *donateWindow;
    SettingWindow *settingWindow;
    QPushButton *CPUStatusBox;
    QPushButton *WootecStatusBox;
    QFont m_defaultFont;
    QVector<QPushButton *> m_appsVector;
    QVector<QPushButton *> m_workspaceVector;
    QVector<QPushButton *> m_teamVector;
    QString m_clientName;
    QIcon m_clientIcon;
};
#endif  // MAINAPP_H
