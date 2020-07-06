#ifndef MONITOR_H
#define MONITOR_H

// Qt lib import
#include <QDateTime>
#include <QMutex>
#include <QObject>
#include <QPointer>
#include <QThread>

class JQCPUMonitor : public QThread {
    Q_OBJECT
    Q_DISABLE_COPY(JQCPUMonitor)

   private:
    JQCPUMonitor() = default;

   public:
    ~JQCPUMonitor() = default;

   public:
    static void initialize();

    static qreal cpuUsagePercentage();

   private:
    void run();

    static void tick();

   private:
    static QPointer<JQCPUMonitor> cpuMonitor_;
    static bool continueFlag_;

    static QMutex mutex_;
    static QList<QPair<qint64, qreal> >
        cpuUsagePercentageRecords_;  // [ { time, percentage }, ... ]
};

#endif  // MONITOR_H
