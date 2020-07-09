#include "SettingWindow.h"

#include <QListWidgetItem>
#include <QMouseEvent>

#include "ui_SettingWindow.h"

SettingWindow::SettingWindow(QWidget *parent)
    : QDialog(parent), ui(new Ui::SettingWindow) {
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->mMoving = false;
    for(int i = this->ui->settingPageStack->count(); i >= 0; i--)
    {
        QWidget* widget = this->ui->settingPageStack->widget(i);
        this->ui->settingPageStack->removeWidget(widget);
        widget->deleteLater();
    }
    QObject::connect(this->ui->menuView, SIGNAL(itemClicked(QListWidgetItem*)), this, SLOT(changePage(QListWidgetItem*)));
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

void SettingWindow::addPage(const QString &name, QWidget *page) {
    auto* item = new QListWidgetItem(name);
    this->ui->menuView->addItem(item);
    this->ui->settingPageStack->addWidget(page);
    this->map[item] = page;
}

void SettingWindow::changePage(QListWidgetItem *item) {
    this->ui->settingPageStack->setCurrentWidget(map[item]);
}
