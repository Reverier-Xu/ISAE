//
// Created by reverier on 2020/7/9.
//

#include "MainAppSettingPage.h"
#include "ui_MainAppSettingPage.h"
#include <QFile>
#include <QDebug>
#include <QCoreApplication>
#include <QtWidgets/QListWidgetItem>

MainAppSettingPage::MainAppSettingPage(QWidget *parent) :
        ISAEPluginSettingWidget(parent), ui(new Ui::MainAppSettingPage) {
    ui->setupUi(this);
    this->m_pluginWidget = (ISAEPluginWidget*)parent;
    this->ui->backgroundImageChooser->setDragEnabled(false);
    this->ui->backgroundImageChooser->setIconSize(QSize(240, 135));
    this->ui->backgroundImageChooser->setSpacing(10);
    this->ui->backgroundImageChooser->setFocusPolicy(Qt::NoFocus);
}

MainAppSettingPage::~MainAppSettingPage() {
}

bool MainAppSettingPage::saveSettings() {
    this->m_settings->clear();
    this->m_settings->beginGroup("MainApp");
    this->m_settings->beginWriteArray("AvailableWallpaper");
    for (int i = 0; i < this->ui->backgroundImageChooser->count(); i++) {
        this->m_settings->setArrayIndex(i);
        this->m_settings->setValue("Wallpaper", this->ui->backgroundImageChooser->item(i)->data(Qt::UserRole));
        this->m_settings->setValue("Name", this->ui->backgroundImageChooser->item(i)->text());
    }
    this->m_settings->endArray();
    // qDebug() << this->ui->backgroundImageChooser->currentItem();
    this->m_settings->setValue("PresentWallpaper", this->ui->backgroundImageChooser->currentItem()->data(Qt::UserRole));
    this->m_settings->setValue("PresentWallpaperName", this->ui->backgroundImageChooser->currentItem()->text());
    this->m_settings->setValue("BlurValue", this->ui->horizontalSlider->value());
    this->m_settings->endGroup();
    this->m_settings->sync();
    return true;
}

bool MainAppSettingPage::loadSettings(const QString &path) {
    this->m_settings = new QSettings(path, QSettings::IniFormat);
    this->m_settings->setIniCodec("UTF-8");
    if (!QFile::exists(path)) {
        this->m_settings->beginGroup("MainApp");
        this->m_settings->beginWriteArray("AvailableWallpaper");
        this->m_settings->setArrayIndex(0);
        this->m_settings->setValue("Wallpaper", ":/wallpapers/wallpaper");
        this->m_settings->setValue("Name", "Default");
        this->m_settings->setArrayIndex(1);
        this->m_settings->setValue("Wallpaper", ":/wallpapers/wallpaper2");
        this->m_settings->setValue("Name", "Blue");
        this->m_settings->endArray();
        this->m_settings->setValue("PresentWallpaper", ":/wallpapers/wallpaper");
        this->m_settings->setValue("PresentWallpaperName", "Default");
        this->m_settings->setValue("BlurValue", "100");
        this->m_settings->endGroup();
        this->m_settings->sync();
    }
    this->drawSettings();
    return true;
}

void MainAppSettingPage::drawSettings() {
    this->m_settings->beginGroup("MainApp");
    int size = this->m_settings->beginReadArray("AvailableWallpaper");
    for (int i = 0; i < size; i++) {
        this->m_settings->setArrayIndex(i);
        // qDebug() << this->m_settings->value("Wallpaper").toString();
        QPixmap pixmap(this->m_settings->value("Wallpaper").toString());
        pixmap = pixmap.scaled(240, 135);
        auto *uItem = new QListWidgetItem(QIcon(pixmap),
                                          this->m_settings->value("Name").toString());
        uItem->setData(Qt::UserRole, this->m_settings->value("Wallpaper").toString());
        this->ui->backgroundImageChooser->addItem(uItem);
    }
    this->m_settings->endArray();
    for (int i = 0; i < this->ui->backgroundImageChooser->count(); i++) {
        if (this->ui->backgroundImageChooser->item(i)->text() ==
            this->m_settings->value("PresentWallpaperName").toString()) {
            this->ui->backgroundImageChooser->item(i)->setSelected(true);
            this->ui->backgroundImageChooser->setCurrentItem(
                    this->ui->backgroundImageChooser->item(i));
        }
    }
    this->ui->horizontalSlider->setValue(this->m_settings->value("BlurValue").toInt());
    this->m_settings->endGroup();
}
