#include "AboutWindow.h"

#include <QMouseEvent>

#include "ui_AboutWindow.h"

AboutWindow::AboutWindow(QWidget *parent) : QDialog(parent), ui(new Ui::AboutWindow) {
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
    this->mMoving = false;
}

/* 窗口移动函数 */
void AboutWindow::mousePressEvent(QMouseEvent *event) {
    this->mMoving = true;
    this->mMovePosition = event->globalPos() - pos();
    return QDialog::mousePressEvent(event);
}

void AboutWindow::mouseMoveEvent(QMouseEvent *event) {
    if (this->mMoving && (event->buttons() & Qt::LeftButton) &&
        (event->globalPos() - mMovePosition).manhattanLength() >
        QApplication::startDragDistance()) {
        move(event->globalPos() - mMovePosition);
        mMovePosition = event->globalPos() - pos();
    }
    return QDialog::mouseMoveEvent(event);
}

void AboutWindow::mouseReleaseEvent(QMouseEvent *event) {
    this->mMoving = false;
    event->accept();
}

AboutWindow::~AboutWindow() { delete ui; }
