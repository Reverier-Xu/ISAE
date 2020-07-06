#include <QApplication>
#include <QSplashScreen>
#include <QThread>

#include "MainApp.h"  //主窗口

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);  // 声明一个Qt应用
    a.setStyle(QString("Fusion"));  // 设置应用基本风格, Fusion可以兼容多平台,
                                    // 实际上所有的样式表都是更改过的
    QImage img;  // 准备启动画面的图片
    img.load(":/imgs/assets/isae-splash.png");
    QSplashScreen splash(QPixmap::fromImage(img));
    splash.show();         // 展示
    QThread::msleep(500);  // TODO: 插件增多之后注释掉此行
                           // 这里仅仅只是为了展示splash的效果.
    MainApp w;             // 声明主窗口, 加载所有插件.
    w.setWindowTitle("ISAE");

    splash.finish(&w);  // 主窗口加载完毕后关掉启动画面
    w.show();           // 让主窗口显示出来
    return a.exec();    // 进入事件循环
}
