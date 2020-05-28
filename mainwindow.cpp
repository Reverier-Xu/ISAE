#include "mainwindow.h"

#include <QLabel>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent)
{
    // Create the dock manager. Because the parent parameter is a QMainWindow
    // the dock manager registers itself as the central widget.
    m_DockManager = new ads::CDockManager(this);

    // Create example content label - this can be any application specific
    // widget
    QLabel* l1 = new QLabel();
    l1->setWordWrap(true);
    l1->setAlignment(Qt::AlignTop | Qt::AlignLeft);
    l1->setText("ISAE C++移植 高级dock停靠系统完成");
    QLabel* l2 = new QLabel();
    l2->setWordWrap(true);
    l2->setAlignment(Qt::AlignTop | Qt::AlignLeft);
    l2->setText("ISAE C++移植 高级dock停靠系统完成");
    QLabel* l3 = new QLabel();
    l3->setWordWrap(true);
    l3->setAlignment(Qt::AlignTop | Qt::AlignLeft);
    l3->setText("ISAE C++移植 高级dock停靠系统完成");

    // Create a dock widget with the title Label 1 and set the created label
    // as the dock widget content
    ads::CDockWidget* DockWidget1 = new ads::CDockWidget("Label 1");
    DockWidget1->setWidget(l1);
    ads::CDockWidget* DockWidget2 = new ads::CDockWidget("Label 2");
    DockWidget2->setWidget(l2);
    ads::CDockWidget* DockWidget3 = new ads::CDockWidget("Label 3");
    DockWidget3->setWidget(l3);

    m_DockManager->addDockWidget(ads::TopDockWidgetArea, DockWidget1);
    m_DockManager->addDockWidget(ads::LeftDockWidgetArea, DockWidget2);
    m_DockManager->addDockWidget(ads::TopDockWidgetArea, DockWidget3);
}

MainWindow::~MainWindow()
{
}
