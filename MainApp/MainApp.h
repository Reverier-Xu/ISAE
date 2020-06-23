#ifndef MAINAPP_H
#define MAINAPP_H

#include <about.h>
#include <donate.h>

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
    MainApp(QWidget *parent = nullptr);
    ~MainApp();

   public slots:
    void changeWindowStatus();
    void pushSideBar();
    void animateSideBar();
    void animateAppList();
    void animateTeamList();
    void animateWorkspaceList();
    void pushAppList();
    void pushTeamList();
    void pushWorkspaceList();
    void showAbout();
    void showDonate();
    void upgradeCPUStatus();

   protected:
    virtual void mousePressEvent(QMouseEvent *event);
    virtual void mouseMoveEvent(QMouseEvent *event);
    virtual void mouseReleaseEvent(QMouseEvent *event);

   private:
    Ui::MainWindow *ui;
    bool mMoving;
    QPoint mMovePosition;
    bool isMaximum;
    bool isSidebarShow;
    bool isAppAreaShow;
    bool isTeamAreaShow;
    bool isWorkspaceAreaShow;
    QTimer sideBarAnimation;
    QTimer appAreaAnimation;
    QTimer teamAreaAnimation;
    QTimer workspaceAreaAnimation;
    QTimer CPUMonitorTimer;
    int startDuration;
    about *aboutWindow;
    donate *donateWindow;
    QPushButton* CPUStatusBox;
    QPushButton* WootecStatusBox;
    QFont defaultFont;
};
#endif  // MAINAPP_H
