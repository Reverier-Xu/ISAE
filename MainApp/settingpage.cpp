#include "settingpage.h"

#include <QMouseEvent>

#include "ui_settingpage.h"

settingpage::settingpage(QWidget *parent) : QDialog(parent), ui(new Ui::settingpage) {
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->mMoving = false;
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
