#include "donate.h"
#include "ui_donate.h"
#include <QMouseEvent>

donate::donate(QWidget *parent) : QDialog(parent), ui(new Ui::donate) {
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->mMoving = false;
}

/* 窗口移动函数 */
void donate::mousePressEvent(QMouseEvent *event) {
    this->mMoving = true;
    this->mMovePosition = event->globalPos() - pos();
    return QDialog::mousePressEvent(event);
}

void donate::mouseMoveEvent(QMouseEvent *event) {
    if (this->mMoving && (event->buttons() & Qt::LeftButton) &&
        (event->globalPos() - mMovePosition).manhattanLength() >
            QApplication::startDragDistance()) {
        move(event->globalPos() - mMovePosition);
        mMovePosition = event->globalPos() - pos();
    }
    return QDialog::mouseMoveEvent(event);
}

void donate::mouseReleaseEvent(QMouseEvent *event) {
    this->mMoving = false;
    event->accept();
}

donate::~donate() { delete ui; }
