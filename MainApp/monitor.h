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

    inline static QString cpuUsagePercentageDisplayString();

    inline static QString cpuUsagePercentageIn5SecondDisplayString();

    inline static QString cpuUsagePercentageIn30SecondDisplayString();

    inline static QString cpuUsagePercentageIn5MinuteDisplayString();

    inline static QString cpuUsagePercentageInTimeDisplayString(
        const qint64 &msecs);

    static qreal cpuUsagePercentage();

    inline static qreal cpuUsagePercentageIn5Second();

    inline static qreal cpuUsagePercentageIn30Second();

    inline static qreal cpuUsagePercentageIn5Minute();

    static qreal cpuUsagePercentageInTime(const qint64 &msecs);

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
