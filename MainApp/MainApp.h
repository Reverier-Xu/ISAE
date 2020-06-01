#ifndef MAINAPP_H
#define MAINAPP_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainApp : public QMainWindow
{
  Q_OBJECT

public:
  MainApp(QWidget *parent = nullptr);
  ~MainApp();

public slots:
    void changeWindowStatus();
    void pushSideBar();

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
};
#endif // MAINAPP_H
