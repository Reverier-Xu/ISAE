//
// Created by reverier on 2020/7/29.
//

#ifndef ISAE_EDITOR_H
#define ISAE_EDITOR_H

#include "ISAEPluginWidget.h"
#include <KTextEditor/View>
#include <KTextEditor/Document>
#include <KTextEditor/Editor>
#include "hexeditor.h"

QT_BEGIN_NAMESPACE
namespace Ui {
    class Editor;
}
QT_END_NAMESPACE

class Editor : public ISAEPluginWidget {
Q_OBJECT
public:
    explicit Editor(QWidget *parent = nullptr, QFlags<Qt::WindowType> flags = Qt::WindowFlags());

    // 接收函数, 由用户自行实现
    bool updateStatus(QVector<QString> info) override { return true; };

    // 应用设置, 由用户自行实现
    bool applySettings() override { return true; };
public slots:

    void setMode(const QString &mode);

private:
    Ui::Editor *ui;
    KTextEditor::View *m_textEditor;
    HexEditor *m_hexEditor;
};


#endif //ISAE_EDITOR_H
