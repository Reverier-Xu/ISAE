#include "about.h"

#include <QMouseEvent>

#include "ui_about.h"

about::about(QWidget *parent) : QDialog(parent), ui(new Ui::about) {
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->mMoving = false;
}

/* 窗口移动函数 */
void about::mousePressEvent(QMouseEvent *event) {
    this->mMoving = true;
    this->mMovePosition = event->globalPos() - pos();
    return QDialog::mousePressEvent(event);
}

void about::mouseMoveEvent(QMouseEvent *event) {
    if (this->mMoving && (event->buttons() & Qt::LeftButton) &&
        (event->globalPos() - mMovePosition).manhattanLength() >
            QApplication::startDragDistance()) {
        move(event->globalPos() - mMovePosition);
        mMovePosition = event->globalPos() - pos();
    }
    return QDialog::mouseMoveEvent(event);
}

void about::mouseReleaseEvent(QMouseEvent *event) {
    this->mMoving = false;
    event->accept();
}

about::~about() { delete ui; }
