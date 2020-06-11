#include "about.h"

#include "ui_about.h"

about::about(QWidget *parent) : QDialog(parent), ui(new Ui::about) {
    ui->setupUi(this);
    this->setWindowFlags(Qt::FramelessWindowHint);
}

about::~about() { delete ui; }
