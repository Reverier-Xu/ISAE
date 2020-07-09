//
// Created by reverier on 2020/7/9.
//

#include "MainAppSettingPage.h"
#include "ui_MainAppSettingPage.h"
#include <QFile>
#include <QDebug>
#include <QCoreApplication>

MainAppSettingPage::MainAppSettingPage(QWidget *parent) :
        QWidget(parent), ui(new Ui::MainAppSettingPage) {
    ui->setupUi(this);
    this->ui->backgroundImageChooser->setDragEnabled(false);
    this->m_settings = nullptr;
    this->ui->backgroundImageChooser->setIconSize(QSize(240, 135));
    this->ui->backgroundImageChooser->setSpacing(10);
    this->ui->backgroundImageChooser->setFocusPolicy(Qt::NoFocus);
}

MainAppSettingPage::~MainAppSettingPage() {
    if (this->isValid())
        this->m_settings->deleteLater();
}

void MainAppSettingPage::saveSetting() {
    this->m_settings->clear();
    this->m_settings->beginGroup("MainApp");
    this->m_settings->beginWriteArray("AvailableWallpaper");
    for (int i = 0; i < this->ui->backgroundImageChooser->count(); i++) {
        this->m_settings->setArrayIndex(i);
        this->m_settings->setValue("Wallpaper", this->ui->backgroundImageChooser->item(i)->data(Qt::UserRole));
        this->m_settings->setValue("Name", this->ui->backgroundImageChooser->item(i)->text());
    }
    this->m_settings->endArray();
    this->m_settings->setValue("PresentWallpaper", this->ui->backgroundImageChooser->currentItem()->data(Qt::UserRole));
    this->m_settings->setValue("PresentWallpaperName", this->ui->backgroundImageChooser->currentItem()->text());
    this->m_settings->setValue("BlurValue", this->ui->horizontalSlider->value());
    if (this->isValid())
        this->m_settings->sync();
}

void MainAppSettingPage::loadSetting(const QString &path) {

    this->m_settings = new QSettings(path, QSettings::IniFormat);
    this->m_settings->setIniCodec("UTF-8");
    if (!QFile::exists(path)) {
        this->m_settings->beginGroup("MainApp");
        this->m_settings->beginWriteArray("AvailableWallpaper");
        this->m_settings->setArrayIndex(0);
        this->m_settings->setValue("Wallpaper", ":/imgs/wallpaper");
        this->m_settings->setValue("Name", "Default");
        this->m_settings->setArrayIndex(1);
        this->m_settings->setValue("Wallpaper", ":/imgs/wallpaper2");
        this->m_settings->setValue("Name", "Blue");
        this->m_settings->endArray();
        this->m_settings->setValue("PresentWallpaper", ":/imgs/wallpaper");
        this->m_settings->setValue("PresentWallpaperName", "Default");
        this->m_settings->setValue("BlurValue", "100");
        this->m_settings->endGroup();
        this->m_settings->sync();
    }
    this->drawSetting();
}


bool MainAppSettingPage::isValid() const {
    return this->m_isValid;
}

void MainAppSettingPage::drawSetting() {
    this->m_settings->beginGroup("MainApp");
    int size = this->m_settings->beginReadArray("AvailableWallpaper");
    for (int i = 0; i < size; i++) {
        this->m_settings->setArrayIndex(i);
        qDebug() << this->m_settings->value("Wallpaper").toString();
        QPixmap pixmap(this->m_settings->value("Wallpaper").toString());
        pixmap = pixmap.scaled(240, 135);
        auto *uItem = new QListWidgetItem(QIcon(pixmap),
                                    this->m_settings->value("Name").toString());
        uItem->setData(Qt::UserRole, this->m_settings->value("Wallpaper").toString());
        this->ui->backgroundImageChooser->addItem(uItem);
    }
    this->m_settings->endArray();
    auto item = this->ui->backgroundImageChooser->findItems(this->m_settings->value("PresentWallpaperName").toString(), Qt::MatchExactly)[0];
    item->setSelected(true);
    this->ui->horizontalSlider->setValue(this->m_settings->value("BlurValue").toInt());
    this->m_settings->endGroup();
}

const QSettings& MainAppSettingPage::setting() {
    return *this->m_settings;
}
