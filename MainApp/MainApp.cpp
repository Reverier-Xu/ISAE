#include "MainApp.h"
#include "ui_MainApp.h"
#include <QtCore/Qt>
#include <QMouseEvent>

MainApp::MainApp(QWidget *parent)
  : QMainWindow(parent)
  , ui(new Ui::MainWindow)
{
  ui->setupUi(this);
  this->setWindowFlags(Qt::FramelessWindowHint);
  this->setAttribute(Qt::WA_StyledBackground);
  this->mMoving = false;
  this->isMaximum = true;
  this->isSidebarShow = true;
  this->ui->appList->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
  this->ui->workspaceList->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
  this->ui->teamList->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
  this->ui->appList->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
  this->ui->workspaceList->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
  this->ui->teamList->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
  this->showMaximized();
  QObject::connect(ui->maxButton, SIGNAL(clicked()), this, SLOT(changeWindowStatus()));
  QObject::connect(ui->welcomeButton,SIGNAL(clicked()), this, SLOT(pushSideBar()));
}

MainApp::~MainApp()
{
  delete ui;
}

void MainApp::mousePressEvent(QMouseEvent *event)
{
  if(this->isMaximum) return;
  this->mMoving = true;
  this->mMovePosition = event->globalPos() - pos();
  return QMainWindow::mousePressEvent(event);
}

void MainApp::mouseMoveEvent(QMouseEvent *event)
{
  if(this->isMaximum) return;
  if (this->mMoving && (event->buttons() & Qt::LeftButton)
          && (event->globalPos()-mMovePosition).manhattanLength() > QApplication::startDragDistance())
    {
      move(event->globalPos()-mMovePosition);
      mMovePosition = event->globalPos() - pos();
    }
    return QMainWindow::mouseMoveEvent(event);
}
void MainApp::mouseReleaseEvent(QMouseEvent *event)
{
  this->mMoving = false;
  event->accept();
}
void MainApp::changeWindowStatus(){
  if(this->isMaximum){
    this->showNormal();
    this->isMaximum = false;
  }
  else{
    this->showMaximized();
    this->isMaximum = true;
  }
}
void MainApp::pushSideBar(){
  if(this->isSidebarShow){
    this->ui->sidebarWidget->setFixedWidth(42);
    this->ui->clientBox->setVisible(false);
    this->isSidebarShow = false;
  }
  else{
    this->ui->sidebarWidget->setFixedWidth(250);
    this->ui->clientBox->setVisible(true);
    this->isSidebarShow = true;
  }
}
