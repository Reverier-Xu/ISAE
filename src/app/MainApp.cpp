//
// Created by reverier on 2020/7/13.
//

#include "MainApp.h"
#include "ui_MainApp.h"
#include <QScrollBar>
#include <DockManager.h>
#include <QFontDatabase>
#include <QtWidgets/QMessageBox>
#include <QMouseEvent>
#include "isaeutils.h"
#include "filemanager.h"
#include "editor.h"
//#include <KTextEditor/Editor>
//#include <KTextEditor/Document>
//#include <KTextEditor/View>

MainApp::MainApp(QWidget *parent, QFlags<Qt::WindowType> flags)
        : ISAEPluginWidget(parent, flags), ui(new Ui::MainApp) {
    ui->setupUi(this);
    // 设置窗口
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->setAttribute(Qt::WA_StyledBackground);
    // 探测文件夹
    MainApp::detectDirs();

    /* 添加字体 */
    QFontDatabase::addApplicationFont(":/fonts/wqy-microhei.ttc");
    QFontDatabase::addApplicationFont(":/fonts/mono.ttf");
    QFontDatabase::addApplicationFont(":/fonts/UI.otf");

    /* 设置窗口logo */
    QImage logo;
    logo.load(":/assets/ISAE.svg");
    this->setWindowIcon(QPixmap::fromImage(logo));

    /* 初始化窗口状态 */
    this->showMaximized();

    /* 初始化侧边栏动画设置 */
    ui->sideBarWidget->setFoldValue(42);
    ui->sideBarWidget->setUnfoldValue(250);
    ui->sideBarWidget->setCurrentAnimateValue(250);
    ui->sideBarWidget->setFolded(false);
    ui->sideBarScrollArea->horizontalScrollBar()->setEnabled(false);

    /* 设置DockManager的配置选项 */
    ads::CDockManager::setConfigFlag(ads::CDockManager::OpaqueSplitterResize, false);
    ads::CDockManager::setConfigFlag(ads::CDockManager::AllTabsHaveCloseButton, true);
    ads::CDockManager::setConfigFlag(ads::CDockManager::FocusHighlighting, true);
    ads::CDockManager::setConfigFlag(ads::CDockManager::DockAreaHasUndockButton, false);

    // 设置默认字体
    this->m_defaultFont.setFamily("WenQuanYi Micro Hei Mono");

    // 设置动画方向
    ui->teamAreaContent->setVertical(true);
    ui->appsAreaContent->setVertical(true);
    ui->workspaceAreaContent->setVertical(true);

    // 初始化外部窗口
    this->setExtendWindow();

    // 应用已保存的设置
    this->m_settingWindow->applySettings();

    // 设置状态栏
    this->setStatusBarButton();

    // StyleSheet
    this->loadStyleSheet(":/stylesheets/RxFluent.qss");

    /* 信号与槽 */
    QObject::connect(ui->maximizedButton, SIGNAL(clicked()), this,
                     SLOT(changeWindowStatus()));
    QObject::connect(ui->closeButton, SIGNAL(clicked()), this,
                     SLOT(close()));
    QObject::connect(ui->minimizedButton, SIGNAL(clicked()), this,
                     SLOT(showMinimized()));
    QObject::connect(ui->sideBarButton, SIGNAL(clicked()), ui->sideBarWidget,
                     SLOT(doFold()));
    QObject::connect(ui->appsAreaButton, SIGNAL(clicked()), ui->appsAreaContent,
                     SLOT(doFold()));
    QObject::connect(ui->workspaceAreaButton, SIGNAL(clicked()), ui->workspaceAreaContent,
                     SLOT(doFold()));
    QObject::connect(ui->teamAreaButton, SIGNAL(clicked()), ui->teamAreaContent,
                     SLOT(doFold()));
    QObject::connect(ui->sideBarWidget, SIGNAL(animationEnded()), this,
                     SLOT(doFoldClient()));
    QObject::connect(ui->settingsButton, SIGNAL(clicked()), this,
                     SLOT(showSettingWindow()));
    /*ads::CDockWidget *DockWidget;
    {
        auto *l = new QWidget();
        editor = KTextEditor::Editor::instance();
        KTextEditor::Document *doc = editor->createDocument(this);
        KTextEditor::View *view = doc->createView(l);

        QObject::connect(ui->settingsButton, SIGNAL(clicked()), this, SLOT(showEditorConf()));

        // Create a dock widget with the title Label 1 and set the created label
        // as the dock widget content
        DockWidget = new ads::CDockWidget("Editor");
        DockWidget->setWidget(view);
    }
    ui->pluginWindowDockArea->addDockWidget(ads::TopDockWidgetArea, DockWidget);

    ads::CDockWidget *DockWidget2;
    {
        auto *l = new QLabel();
        l->setWordWrap(true);
        l->setAlignment(Qt::AlignTop | Qt::AlignLeft);
        l->setText("Hello World~");
        QFont l_font;
        l_font.setFamilies({"JetBrains Mono", "文泉驿等宽微米黑"});
        l_font.setPixelSize(20);
        l->setFont(l_font);
        // Create a dock widget with the title Label 1 and set the created label
        // as the dock widget content
        DockWidget2 = new ads::CDockWidget("Hello World");
        DockWidget2->setWidget(l);
    }
    ads::CDockWidget *DockWidget3;
    {
        auto *l = new QLabel();
        l->setWordWrap(true);
        l->setAlignment(Qt::AlignTop | Qt::AlignLeft);
        l->setText("Preview");
        QFont l_font;
        l_font.setFamilies({"JetBrains Mono", "文泉驿等宽微米黑"});
        l_font.setPixelSize(20);
        l->setFont(l_font);
        // Create a dock widget with the title Label 1 and set the created label
        // as the dock widget content
        DockWidget3 = new ads::CDockWidget("Preview");
        DockWidget3->setWidget(l);
    }
    ui->pluginWindowDockArea->addDockWidget(ads::TopDockWidgetArea, DockWidget2);
    ui->pluginWindowDockArea->addDockWidget(ads::TopDockWidgetArea, DockWidget3);*/
}

void MainApp::loadStyleSheet(const QString &styleSheetFile) {
    QFile file(styleSheetFile);
    file.open(QFile::ReadOnly);
    if (file.isOpen()) {
        QString styleSheet = this->styleSheet();
        styleSheet += QLatin1String(file.readAll());//读取样式表文件
        this->setStyleSheet(styleSheet);//把文件内容传参
        file.close();
    } else {
        QMessageBox::information(this, "警告", "找不到主窗口样式表");
    }
}

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

void MainApp::addPluginButton(QPushButton *button) {
    ui->appsAreaLayout->addWidget(button);
    button->setProperty("RxButtonStyle", "sideBar");
    ui->appsAreaContent->setFixedHeight(ui->appsAreaLayout->count() * 40);
    ui->appsAreaContent->setUnfoldValue(ui->appsAreaLayout->count() * 40);
    button->setMinimumHeight(40);
    button->setMaximumHeight(40);
    button->setIconSize(QSize(24, 24));
    QFont font("文泉驿等宽微米黑", 12);
    button->setFont(font);
}

void MainApp::setStatusBarButton() {
    /* 初始化状态栏 */
    this->statusBar()->setContentsMargins(8, 0, 0, 0);

    this->WootecStatusBox = new QPushButton(this);
    this->WootecStatusBox->setObjectName("WootecStatusBox");
    this->WootecStatusBox->setIcon(
            QIcon::fromTheme(":/assets/online.svg"));
    this->WootecStatusBox->setObjectName("WootecStatusBox");
    this->WootecStatusBox->setIconSize(QSize(24, 20));
    this->WootecStatusBox->setText(QString(" Wootec Cloud  "));
    this->WootecStatusBox->setFont(this->m_defaultFont);
    this->WootecStatusBox->setProperty("RxButtonStyle", "statusBar");
    this->statusBar()->addWidget(this->WootecStatusBox);

    this->CPUStatusBox = new QPushButton(this);
    this->CPUStatusBox->setObjectName("CPUStatusBox");
    this->CPUStatusBox->setIcon(QIcon::fromTheme(":/assets/CPU.svg"));
    this->CPUStatusBox->setIconSize(QSize(22, 20));
    this->CPUStatusBox->setText(QString(" CPU 00.00% "));
    this->CPUStatusBox->setFont(this->m_defaultFont);
    this->CPUStatusBox->setProperty("RxButtonStyle", "statusBar");
    this->statusBar()->addWidget(this->CPUStatusBox);
}

void MainApp::doFoldClient() {
    if (!isClientFold()) {
        ui->clientButton->setFixedHeight(40);
        ui->clientButton->setIconSize(QSize(24, 24));
        setClientFold(true);
    } else {
        ui->clientButton->setFixedHeight(80);
        ui->clientButton->setIconSize(QSize(48, 48));
        setClientFold(false);
    }
}

bool MainApp::isClientFold() const {
    return this->m_isClientFold;
}

void MainApp::setClientFold(bool flag) {
    this->m_isClientFold = flag;
}

bool MainApp::applySettings() {
    // qDebug() << "Triggered MainApp::applySettings()";
    this->m_settings->beginGroup("MainApp");
    // qDebug() << "Prepared image: " + this->m_settings->value("PresentWallpaper").toString();
    this->setBackground(QImage(this->m_settings->value("PresentWallpaper").toString()),
                        this->m_settings->value("BlurValue").toInt());
    this->m_settings->endGroup();
    return true;
}

void MainApp::setBackground(const QImage &image, int blur) {
    // qDebug() << "Triggered MainApp::setBackground()";
    QImage res = blurred(image, image.rect(), blur);
    QPalette palette;
    QPixmap pixmap = QPixmap::fromImage(res);
    palette.setBrush(QPalette::Window, QBrush(pixmap));
    this->setPalette(palette);
}

[[maybe_unused]] void MainApp::showClient(QString name, QIcon icon) {
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
        icon = QIcon::fromTheme(":/assets/a-z/" + pic);
    }
    this->m_clientIcon = icon;
    this->ui->clientButton->setIcon(icon);
    this->ui->clientButton->setIconSize(QSize(48, 48));
}

void MainApp::detectDirs() {
    QDir dir;
    dir.mkpath(QCoreApplication::applicationDirPath() + "/../Data/UserConfig");
}


void MainApp::setExtendWindow() {
    /* 初始化关于页面 */
    this->m_aboutWindow = new AboutWindow(this);
    this->m_aboutWindow->setWindowFlags(Qt::FramelessWindowHint | Qt::Dialog);
    this->m_aboutWindow->setWindowModality(Qt::ApplicationModal);

    /* 初始化捐助页面 */
    this->m_donateWindow = new DonateWindow(this);
    this->m_donateWindow->setWindowFlags(Qt::FramelessWindowHint | Qt::Dialog);
    this->m_donateWindow->setWindowModality(Qt::ApplicationModal);

    /* 初始化设置页面 */
    this->m_settingDialog = new SettingWindow(this);
    this->m_settingDialog->setWindowFlags(Qt::FramelessWindowHint | Qt::Dialog);
    this->m_settingDialog->setWindowModality(Qt::ApplicationModal);

    this->getPlugins();
}

void MainApp::getPlugins() {
    // MainApp
    this->setPluginSettingWindow();
    QAction *act = this->ui->aboutButton->getmenu()->addAction(QString("关于"));
    QObject::connect(act, SIGNAL(triggered()), this, SLOT(showAboutWindow()));
    act = this->ui->aboutButton->getmenu()->addAction(QString("捐助"));
    QObject::connect(act, SIGNAL(triggered()), this, SLOT(showDonateWindow()));

    // FileManager
    auto *fileManager = new FileManager(this);
    this->addPlugin(fileManager);

    // Editor
    auto *editor = new Editor(this);
    this->addPlugin(editor);

}

void MainApp::addPlugin(ISAEPluginWidget *plugin) {
    auto *menuButton = new MenuButton(this);
    this->ui->menuLayout->addWidget(menuButton);
    menuButton->setFixedHeight(32);
    menuButton->setText(plugin->pluginName());
    menuButton->getmenu()->addAction(QString("空菜单"));
    auto *pluginDock = new ads::CDockWidget(plugin->pluginName());
    pluginDock->setWidget(plugin);
    pluginDock->setObjectName(plugin->pluginName());
    this->m_plugins[plugin->pluginName()] = pluginDock;
    ui->pluginWindowDockArea->addDockWidget(ads::RightDockWidgetArea, pluginDock);
    this->m_settingDialog->addPage(plugin->pluginName(), plugin->settingWindow(), plugin);
    auto *appButton = new QPushButton(QIcon(plugin->pluginIcon()), " " + plugin->pluginName(), this);
    this->addPluginButton(appButton);
    QObject::connect(appButton, &QPushButton::clicked, [=]() { showAppDock(plugin->pluginName()); });
}

void MainApp::showAppDock(const QString &plugin) {
    ui->pluginWindowDockArea->findDockWidget(plugin)->toggleView();
}

void MainApp::setPluginSettingWindow() {
    this->m_settingWindow = new MainAppSettingPage(this);
    this->m_settingWindow->loadSettings(QCoreApplication::applicationDirPath() +
                                        "/../Data/UserConfig/MainApp.conf");
    this->m_settingDialog->addPage("主程序", this->m_settingWindow, this);
    this->m_settings = this->m_settingWindow->setting();
}