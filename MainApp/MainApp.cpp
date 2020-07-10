#include "MainApp.h"

#include <QFontDatabase>
#include <QGraphicsEffect>
#include <QGraphicsPixmapItem>
#include <QMouseEvent>          // 移动窗口所需
#include <QPainter>
#include <QtCore/Qt>
#include <QDir>
#include <QCoreApplication>

#include "DockManager.h"        // 高级停靠系统
#include "AboutWindow.h"        // 关于页面
#include "DonateWindow.h"
#include "SettingWindow.h"
#include "isaeutils.h"
#include "monitor.h"
#include "ui_MainApp.h"         // ui文件

MainApp::MainApp(QWidget *parent)
        : ISAEPluginWidget(parent), ui(new Ui::MainWindow) {
    /* 设置布局 */
    ui->setupUi(this);
    this->detectDirs();

    /* 添加字体 */
    QFontDatabase::addApplicationFont(":/imgs/wqy");
    QFontDatabase::addApplicationFont(":/imgs/mono");
    QFontDatabase::addApplicationFont(":/imgs/earthOrbiter");

    /* 设置窗口logo */
    QImage logo;
    logo.load(":/imgs/assets/ISAE.svg");
    this->setWindowIcon(QPixmap::fromImage(logo));

    /* 设置无边框与背景 */
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->setAttribute(Qt::WA_StyledBackground);

    /* 初始化窗口可伸缩部件的大小 */
    this->ui->appsArea->setFixedHeight(0);
    this->ui->teamArea->setFixedHeight(0);
    this->ui->workspaceArea->setFixedHeight(0);
    this->ui->sidebarWidget->setFixedWidth(250);

    /* 初始化动画计时器 */
    this->m_startDuration = 1;
    this->m_sideBarAnimation.setInterval(10);
    this->m_appsAreaAnimation.setInterval(10);
    this->m_teamAreaAnimation.setInterval(10);
    this->m_workspaceAreaAnimation.setInterval(10);

    /* 初始化窗口状态 */
    this->showMaximized();

    /* 设置外部窗口 */
    this->setExtendWindow();

    /* 初始化用户 */
    this->m_clientName = "OFFLINE";
    this->m_clientIcon = QIcon::fromTheme(":/imgs/assets/a-z/offline.svg");

    /* 信号与槽 */
    QObject::connect(ui->maxButton, SIGNAL(clicked()), this,
                     SLOT(changeWindowStatus()));


    QObject::connect(&(this->m_sideBarAnimation), SIGNAL(timeout()),
                     SLOT(sideBarAnimating()));
    QObject::connect(ui->welcomeButton, SIGNAL(clicked()), this,
                     SLOT(activateSideBarAnimation()));

    QObject::connect(&(this->m_appsAreaAnimation), SIGNAL(timeout()),
                     SLOT(appsAreaAnimating()));
    QObject::connect(ui->appsButton, SIGNAL(clicked()), this,
                     SLOT(activateAppsAreaAnimation()));

    QObject::connect(&(this->m_teamAreaAnimation), SIGNAL(timeout()),
                     SLOT(teamAreaAnimating()));
    QObject::connect(ui->teamButton, SIGNAL(clicked()), this,
                     SLOT(activateTeamAreaAnimation()));

    QObject::connect(&(this->m_workspaceAreaAnimation), SIGNAL(timeout()),
                     SLOT(workspaceAreaAnimating()));
    QObject::connect(ui->workspaceButton, SIGNAL(clicked()), this,
                     SLOT(activateWorkspaceAreaAnimation()));

    QObject::connect(&(this->m_CPUMonitorTimer), SIGNAL(timeout()),
                     SLOT(upgradeCPUStatus()));
    QObject::connect(ui->settingsButton, SIGNAL(clicked()), this,
                     SLOT(showSettingWindow()));

    QAction *act = this->ui->aboutButton->getmenu()->addAction(QString("关于"));
    QObject::connect(act, SIGNAL(triggered()), this, SLOT(showAboutWindow()));
    act = this->ui->aboutButton->getmenu()->addAction(QString("捐助"));
    QObject::connect(act, SIGNAL(triggered()), this, SLOT(showDonateWindow()));

    /* 初始化默认字体 */
    this->m_defaultFont.setFamily("WenQuanYi Micro Hei Mono");

    /* 初始化状态栏 */
    this->statusBar()->setContentsMargins(8, 0, 0, 0);

    this->WootecStatusBox = new QPushButton(this);
    this->WootecStatusBox->setObjectName("WootecStatusBox");
    this->WootecStatusBox->setIcon(
            QIcon::fromTheme(":/imgs/assets/online.svg"));
    this->WootecStatusBox->setObjectName("WootecStatusBox");
    this->WootecStatusBox->setIconSize(QSize(24, 20));
    this->WootecStatusBox->setText(QString(" Wootec Cloud  "));
    this->statusBar()->addWidget(this->WootecStatusBox);
    this->WootecStatusBox->setFont(this->m_defaultFont);

    this->CPUStatusBox = new QPushButton(this);
    this->CPUStatusBox->setObjectName("CPUStatusBox");
    this->CPUStatusBox->setIcon(QIcon::fromTheme(":/imgs/assets/CPU.svg"));
    this->CPUStatusBox->setIconSize(QSize(22, 20));
    this->CPUStatusBox->setText(QString(" CPU 00.00% "));
    this->CPUStatusBox->setFont(this->m_defaultFont);
    this->statusBar()->addWidget(this->CPUStatusBox);

    // CPU Monitor
    this->m_CPUMonitorTimer.setInterval(1000);
    JQCPUMonitor::initialize();
    this->m_CPUMonitorTimer.start();

    // 设置应用程序样式
    QFile qssFile(":/imgs/defaultStyle");
    qssFile.open(QFile::ReadOnly);
    QString qss = QLatin1String(qssFile.readAll());
    this->setStyleSheet(qss);
    qssFile.close();

    // 应用设置
    this->applySetting();
}

MainApp::~MainApp() { delete ui; }

/* 窗口移动函数 */
void MainApp::mousePressEvent(QMouseEvent *event) {
    if (this->isMaximized()) return;
    this->m_isMoving = true;
    this->m_MovePosition = event->globalPos() - pos();
    return QMainWindow::mousePressEvent(event);
}

void MainApp::mouseMoveEvent(QMouseEvent *event) {
    if (this->isMaximized()) return;
    if (this->m_isMoving && (event->buttons() & Qt::LeftButton) &&
        (event->globalPos() - m_MovePosition).manhattanLength() >
        QApplication::startDragDistance()) {
        move(event->globalPos() - m_MovePosition);
        m_MovePosition = event->globalPos() - pos();
    }
    return QMainWindow::mouseMoveEvent(event);
}

void MainApp::mouseReleaseEvent(QMouseEvent *event) {
    this->m_isMoving = false;
    event->accept();
}

void MainApp::changeWindowStatus() {
    if (this->isMaximized()) {
        this->showNormal();
    } else {
        this->showMaximized();
    }
}

/* 侧边栏动画函数 */
void MainApp::sideBarAnimating() {
    if (this->m_isSidebarShow) {
        this->ui->clientButton->setIconSize(QSize(24, 24));
        this->ui->clientButton->setText("");
        if (this->ui->clientButton->height() > 36) {
            this->ui->clientButton->setFixedHeight(
                    this->ui->clientButton->height() - 4);
        }
        this->ui->sidebarWidget->setFixedWidth(
                this->ui->sidebarWidget->width() - m_startDuration);

        if (this->ui->sidebarWidget->width() - 42 > 104)
            m_startDuration += 1;
        else if (this->ui->sidebarWidget->width() == 145);
        else
            m_startDuration -= 1;

        if (m_startDuration <= 0) m_startDuration = 1;

        if (this->ui->sidebarWidget->width() <= 42) {
            this->ui->sidebarWidget->setFixedWidth(42);
            this->m_sideBarAnimation.stop();
            this->m_isSidebarShow = false;

            m_startDuration = 1;
        }
    } else {
        this->ui->clientButton->setIconSize(QSize(48, 48));
        this->ui->clientButton->setText(" " + this->m_clientName);
        if (this->ui->clientButton->height() < 80) {
            this->ui->clientButton->setFixedHeight(
                    this->ui->clientButton->height() + 4);
        }
        this->ui->sidebarWidget->setFixedWidth(
                this->ui->sidebarWidget->width() + m_startDuration);

        if (this->ui->sidebarWidget->width() - 42 < 104)
            m_startDuration += 1;
        else if (this->ui->sidebarWidget->width() == 147);
        else
            m_startDuration -= 1;
        if (m_startDuration <= 0) m_startDuration = 1;

        if (this->ui->sidebarWidget->width() >= 250) {
            this->ui->sidebarWidget->setFixedWidth(250);
            this->m_sideBarAnimation.stop();
            this->m_isSidebarShow = true;

            m_startDuration = 1;
        }
    }
}

/* 工作区/分区/团队区分栏展开动画 */
void MainApp::appsAreaAnimating() {
    if (this->m_isAppsAreaShow) {
        if (this->ui->appsArea->height() - this->m_appsVector.size() <= 0) {
            this->ui->appsArea->setFixedHeight(0);
            this->m_appsAreaAnimation.stop();
            this->m_isAppsAreaShow = false;
        } else
            this->ui->appsArea->setFixedHeight(this->ui->appsArea->height() -
                                               this->m_appsVector.size());
    } else {
        this->ui->appsArea->setFixedHeight(this->ui->appsArea->height() +
                                           this->m_appsVector.size());

        if (this->ui->appsArea->height() >= this->m_appsVector.size() * 36 + 3) {
            this->ui->appsArea->setFixedHeight(this->m_appsVector.size() * 36 +
                                               3);
            this->m_appsAreaAnimation.stop();
            this->m_isAppsAreaShow = true;
        }
    }
}

void MainApp::teamAreaAnimating() {
    if (this->m_isTeamAreaShow) {
        if (this->ui->teamArea->height() - this->m_teamVector.size() <= 0) {
            this->ui->teamArea->setFixedHeight(0);
            this->m_teamAreaAnimation.stop();
            this->m_isTeamAreaShow = false;
        } else
            this->ui->teamArea->setFixedHeight(this->ui->teamArea->height() -
                                               this->m_teamVector.size());

    } else {
        this->ui->teamArea->setFixedHeight(this->ui->teamArea->height() +
                                           this->m_teamVector.size());

        if (this->ui->teamArea->height() >= this->m_teamVector.size() * 36 + 3) {
            this->ui->teamArea->setFixedHeight(this->m_teamVector.size() * 36 +
                                               3);
            this->m_teamAreaAnimation.stop();
            this->m_isTeamAreaShow = true;
        }
    }
}

void MainApp::workspaceAreaAnimating() {
    if (this->m_isWorkspaceAreaShow) {
        if (this->ui->workspaceArea->height() - this->m_workspaceVector.size() <=
            0) {
            this->ui->workspaceArea->setFixedHeight(0);
            this->m_workspaceAreaAnimation.stop();
            this->m_isWorkspaceAreaShow = false;
        } else
            this->ui->workspaceArea->setFixedHeight(
                    this->ui->workspaceArea->height() -
                    this->m_workspaceVector.size());
    } else {
        this->ui->workspaceArea->setFixedHeight(
                this->ui->workspaceArea->height() + this->m_workspaceVector.size());

        if (this->ui->workspaceArea->height() >=
            this->m_workspaceVector.size() * 36 + 3) {
            this->ui->workspaceArea->setFixedHeight(
                    this->m_workspaceVector.size() * 36 + 3);
            this->m_workspaceAreaAnimation.stop();
            this->m_isWorkspaceAreaShow = true;
        }
    }
}

/* 显示关于页 */
void MainApp::showAboutWindow() { this->aboutWindow->show(); }

void MainApp::showDonateWindow() { this->donateWindow->show(); }

void MainApp::showSettingWindow() { this->settingWindow->show(); }

void MainApp::upgradeCPUStatus() {
    QString info = " CPU ";
    info += QString::number(JQCPUMonitor::cpuUsagePercentage() * 100, 'f', 2)
                    .rightJustified(5, '0') +
            "% ";
    this->CPUStatusBox->setText(info);
}

void MainApp::setBackground(const QImage &image, int blur) {
    QImage res = blurred(image, image.rect(), blur);
    QPalette palette;
    QPixmap pixmap = QPixmap::fromImage(res);
    palette.setBrush(QPalette::Background, QBrush(pixmap));
    this->setPalette(palette);
}

void MainApp::addApp(const QIcon &icon, const QString &name) {
    auto *app = new QPushButton(this);
    app->setIcon(icon);
    app->setText(" " + name);
    app->setObjectName("apps");
    app->setIconSize(QSize(24, 24));
    app->setMinimumHeight(36);
    app->setMaximumHeight(36);
    this->ui->appsAreaLayout->addWidget(app);
    this->m_appsVector.push_back(app);
}

void MainApp::addWorkspace(const QIcon &icon, const QString &name) {
    auto *app = new QPushButton(this);
    app->setIcon(icon);
    app->setText(" " + name);
    app->setObjectName("apps");
    app->setIconSize(QSize(24, 24));
    app->setMinimumHeight(36);
    app->setMaximumHeight(36);
    this->ui->workspaceAreaLayout->addWidget(app);
    this->m_workspaceVector.push_back(app);
}

void MainApp::addTeam(const QIcon &icon, const QString &name) {
    auto *app = new QPushButton(this);
    app->setIcon(icon);
    app->setText(" " + name);
    app->setObjectName("apps");
    app->setIconSize(QSize(24, 24));
    app->setMinimumHeight(36);
    app->setMaximumHeight(36);
    this->ui->teamAreaLayout->addWidget(app);
    this->m_teamVector.push_back(app);
}

void MainApp::showClient(QString name, QIcon icon) {
    this->ui->clientButton->setText(" " + name);
    this->m_clientName = name;
    if (icon.isNull()) {
        QCharRef x = name[0];
        QString pic;
        x = x.toLower();
        if (!x.isLetterOrNumber()) {
            pic = "nopic.svg";
        } else {
            pic = x + ".svg";
        }
        icon = QIcon::fromTheme(":/imgs/assets/a-z/" + pic);
    }
    this->m_clientIcon = icon;
    this->ui->clientButton->setIcon(icon);
    this->ui->clientButton->setIconSize(QSize(48, 48));
}

void MainApp::activateSideBarAnimation() {
    this->m_sideBarAnimation.start();
}

void MainApp::activateAppsAreaAnimation() {
    this->m_appsAreaAnimation.start();
}

void MainApp::activateTeamAreaAnimation() {
    this->m_teamAreaAnimation.start();
}

void MainApp::activateWorkspaceAreaAnimation() {
    this->m_workspaceAreaAnimation.start();
}

void MainApp::setExtendWindow() {
    /* 初始化关于页面 */
    this->aboutWindow = new AboutWindow(this);
    this->aboutWindow->setWindowFlags(Qt::FramelessWindowHint | Qt::Dialog);
    this->aboutWindow->setWindowModality(Qt::ApplicationModal);

    /* 初始化捐助页面 */
    this->donateWindow = new DonateWindow(this);
    this->donateWindow->setWindowFlags(Qt::FramelessWindowHint | Qt::Dialog);
    this->donateWindow->setWindowModality(Qt::ApplicationModal);

    /* 初始化设置页面 */
    this->settingWindow = new SettingWindow(this);
    this->settingWindow->setWindowFlags(Qt::FramelessWindowHint | Qt::Dialog);
    this->settingWindow->setWindowModality(Qt::ApplicationModal);

    this->getPlugins();
}

void MainApp::getPlugins() {
    this->setPluginSettingWindow();
}

void MainApp::setPluginSettingWindow() {
    this->settingPage = new MainAppSettingPage();
    this->settingPage->loadSetting(QCoreApplication::applicationDirPath() + "/../Data/UserConfig/MainApp.conf");
    this->settingWindow->addPage("主程序", this->settingPage, this);
    this->m_settings = this->settingPage->setting();
}

void MainApp::detectDirs() {
    QDir dir;
    qDebug() << QCoreApplication::applicationDirPath();
    dir.mkpath(QCoreApplication::applicationDirPath() + "/../Data/UserConfig");
}

void MainApp::applySetting() {
    this->m_settings->beginGroup("MainApp");
    this->setBackground(QImage(this->m_settings->value("PresentWallpaper").toString()), this->m_settings->value("BlurValue").toInt());
    this->m_settings->endGroup();
}
