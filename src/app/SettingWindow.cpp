#include "SettingWindow.h"

#include <QListWidgetItem>
#include <QMouseEvent>
#include <QDebug>
#include "ui_SettingWindow.h"

SettingWindow::SettingWindow(QWidget *parent)
    : QDialog(parent), ui(new Ui::SettingWindow) {
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->mMoving = false;
    this->clearPages();
    QObject::connect(this->ui->menuView, SIGNAL(itemClicked(QListWidgetItem*)), this, SLOT(changePage(QListWidgetItem*)));
    QObject::connect(this->ui->saveButton, SIGNAL(clicked()), this, SLOT(saveSettings()));
    QObject::connect(this->ui->applyButton, SIGNAL(clicked()), this, SLOT(applySettings()));
    QObject::connect(this->ui->cancelButton, SIGNAL(clicked()), this, SLOT(close()));
    QObject::connect(this->ui->saveButton, SIGNAL(clicked()), this, SLOT(close()));
}

/* 窗口移动函数 */
void SettingWindow::mousePressEvent(QMouseEvent *event) {
    this->mMoving = true;
    this->mMovePosition = event->globalPos() - pos();
    return QDialog::mousePressEvent(event);
}

void SettingWindow::mouseMoveEvent(QMouseEvent *event) {
    if (this->mMoving && (event->buttons() & Qt::LeftButton) &&
        (event->globalPos() - mMovePosition).manhattanLength() >
            QApplication::startDragDistance()) {
        move(event->globalPos() - mMovePosition);
        mMovePosition = event->globalPos() - pos();
    }
    return QDialog::mouseMoveEvent(event);
}

void SettingWindow::mouseReleaseEvent(QMouseEvent *event) {
    this->mMoving = false;
    event->accept();
}

SettingWindow::~SettingWindow() { delete ui; }

void SettingWindow::addPage(const QString &name, ISAEPluginSettingWidget *page, ISAEPluginWidget *Plugin) {
    auto* item = new QListWidgetItem(name);
    this->ui->menuView->addItem(item);
    this->ui->settingPageStack->addWidget((QWidget*)page);
    this->settingPageMap[name] = page;
    this->pluginMap[name] = Plugin;
}

void SettingWindow::changePage(QListWidgetItem *item) {
    this->ui->settingPageStack->setCurrentWidget((QWidget*)settingPageMap[item->text()]);
}

void SettingWindow::saveSettings() {
    qDebug() << "Triggered SettingWindow::saveSettings()";
    for (auto i : this->settingPageMap) {
        i->saveSettings();
    }
    for (auto i : this->pluginMap) {
        i->applySettings();
    }
}

void SettingWindow::applySettings() {
    qDebug() << "Triggered SettingWindow::applySettings()";
    for (auto i : this->settingPageMap) {
        i->saveSettings();
    }
    for (auto i : this->pluginMap) {
        i->applySettings();
    }
}

void SettingWindow::clearPages() {
    for(int i = this->ui->settingPageStack->count(); i >= 0; i--)
    {
        QWidget* widget = this->ui->settingPageStack->widget(i);
        this->ui->settingPageStack->removeWidget(widget);
        widget->deleteLater();
    }
    this->ui->menuView->clear();
}
