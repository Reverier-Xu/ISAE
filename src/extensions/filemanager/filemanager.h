//
// Created by reverier on 2020/7/29.
//

#ifndef ISAE_FILEMANAGER_H
#define ISAE_FILEMANAGER_H

#include "ISAEPluginWidget.h"
#include <QFileSystemModel>

QT_BEGIN_NAMESPACE
namespace Ui {
    class FileManager;
}
QT_END_NAMESPACE

class FileManager : public ISAEPluginWidget {
Q_OBJECT
public:
    explicit FileManager(QWidget *parent = nullptr, QFlags<Qt::WindowType> flags = Qt::WindowFlags());

    ~FileManager() override = default;

    // 接收函数, 由用户自行实现
    bool updateStatus(QVector<QString> info) override;

    // 应用设置, 由用户自行实现
    bool applySettings() override;

    bool openPath(const QString &path);

public slots:

    void doFoldSearch();

    void doFoldStack();

private:
    Ui::FileManager *ui;
    bool m_isSearchFolded {false};
    bool m_isStackFolded {false};
    QFileSystemModel *m_model {};

};


#endif //ISAE_FILEMANAGER_H
