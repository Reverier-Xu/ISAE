#include "MainApp.h"
#include "ui_MainApp.h"
#include <QtCore/Qt>
#include <QMouseEvent>
#include <iostream>
#include "DockManager.h"

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
  this->isAppAreaShow = false;
  this->isTeamAreaShow = false;
  this->isWorkspaceAreaShow = false;
  this->ui->appsArea->setFixedHeight(0);
  this->ui->teamArea->setFixedHeight(0);
  this->ui->workspaceArea->setFixedHeight(0);
  this->ui->sidebarWidget->setFixedWidth(250);
  this->startDuration = 1;
  this->sideBarAnimation.setInterval(10);
  this->appAreaAnimation.setInterval(10);
  this->teamAreaAnimation.setInterval(10);
  this->workspaceAreaAnimation.setInterval(10);
  this->showMaximized();
  QObject::connect(ui->maxButton, SIGNAL(clicked()), this, SLOT(changeWindowStatus()));
  QObject::connect(&(this->sideBarAnimation), SIGNAL(timeout()), SLOT(animateSideBar()));
  QObject::connect(ui->welcomeButton,SIGNAL(clicked()), this, SLOT(pushSideBar()));
  QObject::connect(&(this->appAreaAnimation), SIGNAL(timeout()), SLOT(animateAppList()));
  QObject::connect(ui->appsButton,SIGNAL(clicked()), this, SLOT(pushAppList()));
  QObject::connect(&(this->teamAreaAnimation), SIGNAL(timeout()), SLOT(animateTeamList()));
  QObject::connect(ui->teamButton,SIGNAL(clicked()), this, SLOT(pushTeamList()));
  QObject::connect(&(this->workspaceAreaAnimation), SIGNAL(timeout()), SLOT(animateWorkspaceList()));
  QObject::connect(ui->workspaceButton,SIGNAL(clicked()), this, SLOT(pushWorkspaceList()));
}

MainApp::~MainApp()
{
  delete ui;
}
/* 窗口移动函数 */
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

/* 侧边栏动画函数 */
void MainApp::pushSideBar(){
  this->sideBarAnimation.start();
}

void MainApp::animateSideBar(){
  if(this->isSidebarShow){
    //std::cout << startDuration << ", " << this->ui->sidebarWidget->width() << std::endl;

    this->ui->sidebarWidget->setFixedWidth(this->ui->sidebarWidget->width()-startDuration);

    if(this->ui->sidebarWidget->width() - 42 > 104) startDuration += 1;
    else if (this->ui->sidebarWidget->width() == 145);
    else startDuration -= 1;

    if (startDuration <= 0) startDuration = 1;

    if(this->ui->sidebarWidget->width()<=42){
      this->ui->sidebarWidget->setFixedWidth(42);
      this->sideBarAnimation.stop();
      this->isSidebarShow = false;

      startDuration = 1;
    }
  } else {
    this->ui->sidebarWidget->setFixedWidth(this->ui->sidebarWidget->width()+startDuration);

    if(this->ui->sidebarWidget->width() - 42 < 104) startDuration += 1;
    else if (this->ui->sidebarWidget->width() == 147);
    else startDuration -= 1;

    if (startDuration <= 0) startDuration = 1;

    if(this->ui->sidebarWidget->width()>=250){
      this->ui->sidebarWidget->setFixedWidth(250);
      this->sideBarAnimation.stop();
      this->isSidebarShow = true;

      startDuration = 1;
    }
  }
}

void MainApp::pushAppList(){
  this->appAreaAnimation.start();
}

void MainApp::animateAppList(){
  if(this->isAppAreaShow){
    //std::cout << startDuration << ", " << this->ui->sidebarWidget->width() << std::endl;

    this->ui->appsArea->setFixedHeight(this->ui->appsArea->height()-12);

    if(this->ui->appsArea->height()<=0){
      this->ui->appsArea->setFixedHeight(0);
      this->appAreaAnimation.stop();
      this->isAppAreaShow = false;
    }
  } else {

    this->ui->appsArea->setFixedHeight(this->ui->appsArea->height()+12);

    if(this->ui->appsArea->height()>=150){
      this->ui->appsArea->setFixedHeight(150);
      this->appAreaAnimation.stop();
      this->isAppAreaShow = true;
    }
  }
}
void MainApp::pushTeamList(){
  this->teamAreaAnimation.start();
}

void MainApp::animateTeamList(){
  if(this->isTeamAreaShow){
    //std::cout << startDuration << ", " << this->ui->sidebarWidget->width() << std::endl;

    this->ui->teamArea->setFixedHeight(this->ui->teamArea->height()-12);

    if(this->ui->teamArea->height()<=0){
      this->ui->teamArea->setFixedHeight(0);
      this->teamAreaAnimation.stop();
      this->isTeamAreaShow = false;
    }
  } else {

    this->ui->teamArea->setFixedHeight(this->ui->teamArea->height()+12);

    if(this->ui->teamArea->height()>=150){
      this->ui->teamArea->setFixedHeight(150);
      this->teamAreaAnimation.stop();
      this->isTeamAreaShow = true;
    }
  }
}
void MainApp::pushWorkspaceList(){
  this->workspaceAreaAnimation.start();
}

void MainApp::animateWorkspaceList(){
  if(this->isWorkspaceAreaShow){
    //std::cout << startDuration << ", " << this->ui->sidebarWidget->width() << std::endl;

    this->ui->workspaceArea->setFixedHeight(this->ui->workspaceArea->height()-12);

    if(this->ui->workspaceArea->height()<=0){
      this->ui->workspaceArea->setFixedHeight(0);
      this->workspaceAreaAnimation.stop();
      this->isWorkspaceAreaShow = false;
    }
  } else {

    this->ui->workspaceArea->setFixedHeight(this->ui->workspaceArea->height()+12);

    if(this->ui->workspaceArea->height()>=150){
      this->ui->workspaceArea->setFixedHeight(150);
      this->workspaceAreaAnimation.stop();
      this->isWorkspaceAreaShow = true;
    }
  }
}
