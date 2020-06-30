#include "settingpage.h"

#include <QMouseEvent>

#include "settings.h"  // 引入全局设置文件
#include "ui_settingpage.h"

settingpage::settingpage(QWidget *parent)
    : QDialog(parent), ui(new Ui::settingpage) {
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->mMoving = false;

    // 清空QStackWidget自带的几个页面
    for (int i = this->ui->settingPageStack->count(); i >= 0; i--) {
        QWidget *widget = this->ui->settingPageStack->widget(i);
        this->ui->settingPageStack->removeWidget(widget);
        widget->deleteLater();
    }
}

/* 窗口移动函数 */
void settingpage::mousePressEvent(QMouseEvent *event) {
    this->mMoving = true;
    this->mMovePosition = event->globalPos() - pos();
    return QDialog::mousePressEvent(event);
}

void settingpage::mouseMoveEvent(QMouseEvent *event) {
    if (this->mMoving && (event->buttons() & Qt::LeftButton) &&
        (event->globalPos() - mMovePosition).manhattanLength() >
            QApplication::startDragDistance()) {
        move(event->globalPos() - mMovePosition);
        mMovePosition = event->globalPos() - pos();
    }
    return QDialog::mouseMoveEvent(event);
}

void settingpage::mouseReleaseEvent(QMouseEvent *event) {
    this->mMoving = false;
    event->accept();
}

settingpage::~settingpage() { delete ui; }

// 注册设置页面
void settingpage::registerSetting() {
    QMapIterator<QString, QSettings *> iter(globalSettings);
    while (iter.hasNext()) {
        iter.next();
        QWidget *widget = new QWidget(this, Qt::WindowFlags());
        widget->setObjectName(iter.key());
        QSettings *settings = iter.value();
        QTreeWidgetItem *rootItem = new QTreeWidgetItem(this->ui->menuView);
        rootItem->setText(0, iter.key());
        QObject::connect(this, SIGNAL(itemClicked(QTreeWidgetItem *, int)),
                         SLOT(changePage(QTreeWidgetItem *, widget)));
    }
}

void settingpage::changePage(QTreeWidgetItem *item, QWidget *widget) {
    this->ui->settingPageStack->setCurrentWidget(widget);
}