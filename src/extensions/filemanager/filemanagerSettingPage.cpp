//
// Created by reverier on 2020/7/29.
//

#include "filemanagerSettingPage.h"
#include "ui_filemanagerSettingPage.h"

FileManagerSettingPage::FileManagerSettingPage(QWidget *parent) :
        ISAEPluginSettingWidget(parent), ui(new Ui::FileManagerSettingPage) {
    ui->setupUi(this);
}
