#include "DonateWindow.h"

#include <QMouseEvent>

#include "ui_DonateWindow.h"

DonateWindow::DonateWindow(QWidget *parent) : QDialog(parent), ui(new Ui::DonateWindow) {
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->mMoving = false;
}

/* 窗口移动函数 */
void DonateWindow::mousePressEvent(QMouseEvent *event) {
    this->mMoving = true;
    this->mMovePosition = event->globalPos() - pos();
    return QDialog::mousePressEvent(event);
}

void DonateWindow::mouseMoveEvent(QMouseEvent *event) {
    if (this->mMoving && (event->buttons() & Qt::LeftButton) &&
        (event->globalPos() - mMovePosition).manhattanLength() >
            QApplication::startDragDistance()) {
        move(event->globalPos() - mMovePosition);
        mMovePosition = event->globalPos() - pos();
    }
    return QDialog::mouseMoveEvent(event);
}

void DonateWindow::mouseReleaseEvent(QMouseEvent *event) {
    this->mMoving = false;
    event->accept();
}

DonateWindow::~DonateWindow() { delete ui; }
