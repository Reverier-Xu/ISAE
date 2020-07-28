//
// Created by reverier on 2020/7/13.
//

#include <QApplication>
#include <QSplashScreen>
#include <QThread>

#include "MainApp.h"  //主窗口

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);                // 声明一个Qt应用
    QApplication::setStyle(QString("Fusion"));  // 设置应用基本风格, Fusion可以兼容多平台
                           // 实际上所有的样式表都是更改过的
    QImage img;            // 准备启动画面的图片
    img.load(":/assets/isae-splash.png");
    QSplashScreen splash(QPixmap::fromImage(img));
    splash.show();         // 展示
    QThread::msleep(500);  // 这里仅仅只是为了展示splash的效果.
    MainApp w;             // 声明主窗口, 加载所有插件.
    w.show();
    splash.finish(&w);

    return QApplication::exec();    // 进入事件循环
}
