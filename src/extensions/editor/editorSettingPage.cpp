//
// Created by reverier on 2020/7/29.
//

#include "editorSettingPage.h"
#include "ui_editorSettingPage.h"
#include <KTextEditor/Editor>
#include <KTextEditor/ConfigPage>
#include <KTextEditor/Document>

EditorSettingPage::EditorSettingPage(QWidget *parent) :
        ISAEPluginSettingWidget(parent), ui(new Ui::EditorSettingPage) {
    ui->setupUi(this);
    ui->pageStack->clear();
}

void EditorSettingPage::addPage(QWidget *widget, const QString& name) {
    this->ui->pageStack->addTab(widget, name);
}

bool EditorSettingPage::saveSettings() {
    for (int i = 0; i < 4; i++){
        auto page = (KTextEditor::ConfigPage*)ui->pageStack->widget(i);
        page->apply();
    }
    return true;
}
