#include <QMainWindow>
#include "DockManager.h"

namespace Ui {
    class MainWindow;
}

class MainWindow : public QMainWindow
{
Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui{};

    // The main container for docking
    ads::CDockManager* m_DockManager;
};