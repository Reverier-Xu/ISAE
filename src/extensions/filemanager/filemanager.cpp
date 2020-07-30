//
// Created by reverier on 2020/7/29.
//

#include "filemanager.h"
#include "ui_filemanager.h"
#include "filemanagerSettingPage.h"
#include <QFileSystemModel>
#include <QtWidgets/QFileDialog>
#include <QtWidgets/QTreeWidgetItem>

FileManager::FileManager(QWidget *parent, QFlags<Qt::WindowType> flags) :
        ISAEPluginWidget(parent, flags), ui(new Ui::FileManager) {
    ui->setupUi(this);
    this->setPluginName("文件管理");
    this->m_settingWindow = new FileManagerSettingPage(this);
    this->m_settings = new QSettings();
    QObject::connect(ui->searchAreaButton, SIGNAL(clicked()), SLOT(doFoldSearch()));
    QObject::connect(ui->tempStackButton, SIGNAL(clicked()), SLOT(doFoldStack()));
    ui->splitter->setChildrenCollapsible(false);
    openPath(QDir::homePath());
    this->m_icon = ":/assets/folder.svg";
    QObject::connect(ui->folderButton, SIGNAL(clicked()), SLOT(openFolder()));
}

bool FileManager::openPath(const QString &path) {
    this->m_model = new QFileSystemModel;
    QDir dir(path);
    if (!dir.exists(path)) return false;
    this->m_model->setRootPath(path);
    ui->fileExplorerBox->setModel(this->m_model);
    ui->fileExplorerBox->setRootIndex(this->m_model->index(path));
    ui->fileExplorerBox->setColumnHidden(1, true);
    ui->fileExplorerBox->setColumnHidden(2, true);
    ui->fileExplorerBox->setColumnHidden(3, true);
    ui->fileExplorerBox->setColumnHidden(4, true);
    ui->fileExplorerBox->header()->hide();
    ui->folderButton->setText(dir.dirName());
    return true;
}

void FileManager::openFolder() {
    QString dir = QFileDialog::getExistingDirectory(this, tr("打开文件夹"),
                                                    this->m_model->rootPath(),
                                                    QFileDialog::ShowDirsOnly
                                                    | QFileDialog::DontResolveSymlinks);
    if (dir == "") return;
    openPath(dir);
}

bool FileManager::updateStatus(QVector<QString> info) {
    return true;
}

bool FileManager::applySettings() {
    return true;
}

void FileManager::doFoldSearch() {
    if (this->m_isSearchFolded) {
        ui->searchAreaWidget->show();
        this->m_isSearchFolded = false;
        ui->search->setMaximumHeight(3200);
    } else {
        ui->searchAreaWidget->hide();
        this->m_isSearchFolded = true;
        ui->search->setMaximumHeight(32);
    }
}

void FileManager::doFoldStack() {
    if (this->m_isStackFolded) {
        ui->tempStackArea->show();
        this->m_isStackFolded = false;
        ui->tempStack->setMaximumHeight(3200);
    } else {
        ui->tempStackArea->hide();
        this->m_isStackFolded = true;
        ui->tempStack->setMaximumHeight(32);
    }
}
