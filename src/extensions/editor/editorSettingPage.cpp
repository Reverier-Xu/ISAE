//
// Created by reverier on 2020/7/29.
//

#include "editorSettingPage.h"
#include "ui_editorSettingPage.h"

EditorSettingPage::EditorSettingPage(QWidget *parent) :
        ISAEPluginSettingWidget(parent), ui(new Ui::EditorSettingPage) {
    ui->setupUi(this);
}
