#include "MainApp.h"

#include <QApplication>

int main(int argc, char *argv[])
{
  QApplication a(argc, argv);
  a.setStyle(QString("Fusion"));
  MainApp w;
  w.show();
  return a.exec();
}
