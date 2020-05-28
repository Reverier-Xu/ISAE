/****************************************************************************
** Meta object code from reading C++ file 'DockManager.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.14.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "DockManager.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'DockManager.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.14.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_ads__CDockManager_t {
    QByteArrayData data[20];
    char stringdata0[332];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_ads__CDockManager_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_ads__CDockManager_t qt_meta_stringdata_ads__CDockManager = {
    {
QT_MOC_LITERAL(0, 0, 17), // "ads::CDockManager"
QT_MOC_LITERAL(1, 18, 22), // "perspectiveListChanged"
QT_MOC_LITERAL(2, 41, 0), // ""
QT_MOC_LITERAL(3, 42, 19), // "perspectivesRemoved"
QT_MOC_LITERAL(4, 62, 14), // "restoringState"
QT_MOC_LITERAL(5, 77, 13), // "stateRestored"
QT_MOC_LITERAL(6, 91, 18), // "openingPerspective"
QT_MOC_LITERAL(7, 110, 15), // "PerspectiveName"
QT_MOC_LITERAL(8, 126, 17), // "perspectiveOpened"
QT_MOC_LITERAL(9, 144, 21), // "floatingWidgetCreated"
QT_MOC_LITERAL(10, 166, 23), // "CFloatingDockContainer*"
QT_MOC_LITERAL(11, 190, 14), // "FloatingWidget"
QT_MOC_LITERAL(12, 205, 15), // "dockAreaCreated"
QT_MOC_LITERAL(13, 221, 16), // "CDockAreaWidget*"
QT_MOC_LITERAL(14, 238, 8), // "DockArea"
QT_MOC_LITERAL(15, 247, 26), // "dockWidgetAboutToBeRemoved"
QT_MOC_LITERAL(16, 274, 12), // "CDockWidget*"
QT_MOC_LITERAL(17, 287, 10), // "DockWidget"
QT_MOC_LITERAL(18, 298, 17), // "dockWidgetRemoved"
QT_MOC_LITERAL(19, 316, 15) // "openPerspective"

    },
    "ads::CDockManager\0perspectiveListChanged\0"
    "\0perspectivesRemoved\0restoringState\0"
    "stateRestored\0openingPerspective\0"
    "PerspectiveName\0perspectiveOpened\0"
    "floatingWidgetCreated\0CFloatingDockContainer*\0"
    "FloatingWidget\0dockAreaCreated\0"
    "CDockAreaWidget*\0DockArea\0"
    "dockWidgetAboutToBeRemoved\0CDockWidget*\0"
    "DockWidget\0dockWidgetRemoved\0"
    "openPerspective"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_ads__CDockManager[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
      11,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
      10,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   69,    2, 0x06 /* Public */,
       3,    0,   70,    2, 0x06 /* Public */,
       4,    0,   71,    2, 0x06 /* Public */,
       5,    0,   72,    2, 0x06 /* Public */,
       6,    1,   73,    2, 0x06 /* Public */,
       8,    1,   76,    2, 0x06 /* Public */,
       9,    1,   79,    2, 0x06 /* Public */,
      12,    1,   82,    2, 0x06 /* Public */,
      15,    1,   85,    2, 0x06 /* Public */,
      18,    1,   88,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
      19,    1,   91,    2, 0x0a /* Public */,

 // signals: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::QString,    7,
    QMetaType::Void, QMetaType::QString,    7,
    QMetaType::Void, 0x80000000 | 10,   11,
    QMetaType::Void, 0x80000000 | 13,   14,
    QMetaType::Void, 0x80000000 | 16,   17,
    QMetaType::Void, 0x80000000 | 16,   17,

 // slots: parameters
    QMetaType::Void, QMetaType::QString,    7,

       0        // eod
};

void ads::CDockManager::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<CDockManager *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->perspectiveListChanged(); break;
        case 1: _t->perspectivesRemoved(); break;
        case 2: _t->restoringState(); break;
        case 3: _t->stateRestored(); break;
        case 4: _t->openingPerspective((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->perspectiveOpened((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 6: _t->floatingWidgetCreated((*reinterpret_cast< CFloatingDockContainer*(*)>(_a[1]))); break;
        case 7: _t->dockAreaCreated((*reinterpret_cast< CDockAreaWidget*(*)>(_a[1]))); break;
        case 8: _t->dockWidgetAboutToBeRemoved((*reinterpret_cast< CDockWidget*(*)>(_a[1]))); break;
        case 9: _t->dockWidgetRemoved((*reinterpret_cast< CDockWidget*(*)>(_a[1]))); break;
        case 10: _t->openPerspective((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 6:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<int*>(_a[0]) = -1; break;
            case 0:
                *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< CFloatingDockContainer* >(); break;
            }
            break;
        case 8:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<int*>(_a[0]) = -1; break;
            case 0:
                *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< CDockWidget* >(); break;
            }
            break;
        case 9:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<int*>(_a[0]) = -1; break;
            case 0:
                *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< CDockWidget* >(); break;
            }
            break;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (CDockManager::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::perspectiveListChanged)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (CDockManager::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::perspectivesRemoved)) {
                *result = 1;
                return;
            }
        }
        {
            using _t = void (CDockManager::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::restoringState)) {
                *result = 2;
                return;
            }
        }
        {
            using _t = void (CDockManager::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::stateRestored)) {
                *result = 3;
                return;
            }
        }
        {
            using _t = void (CDockManager::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::openingPerspective)) {
                *result = 4;
                return;
            }
        }
        {
            using _t = void (CDockManager::*)(const QString & );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::perspectiveOpened)) {
                *result = 5;
                return;
            }
        }
        {
            using _t = void (CDockManager::*)(CFloatingDockContainer * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::floatingWidgetCreated)) {
                *result = 6;
                return;
            }
        }
        {
            using _t = void (CDockManager::*)(CDockAreaWidget * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::dockAreaCreated)) {
                *result = 7;
                return;
            }
        }
        {
            using _t = void (CDockManager::*)(CDockWidget * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::dockWidgetAboutToBeRemoved)) {
                *result = 8;
                return;
            }
        }
        {
            using _t = void (CDockManager::*)(CDockWidget * );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&CDockManager::dockWidgetRemoved)) {
                *result = 9;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject ads::CDockManager::staticMetaObject = { {
    QMetaObject::SuperData::link<CDockContainerWidget::staticMetaObject>(),
    qt_meta_stringdata_ads__CDockManager.data,
    qt_meta_data_ads__CDockManager,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *ads::CDockManager::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *ads::CDockManager::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_ads__CDockManager.stringdata0))
        return static_cast<void*>(this);
    return CDockContainerWidget::qt_metacast(_clname);
}

int ads::CDockManager::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = CDockContainerWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 11)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 11;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 11)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 11;
    }
    return _id;
}

// SIGNAL 0
void ads::CDockManager::perspectiveListChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void ads::CDockManager::perspectivesRemoved()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void ads::CDockManager::restoringState()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void ads::CDockManager::stateRestored()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void ads::CDockManager::openingPerspective(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 4, _a);
}

// SIGNAL 5
void ads::CDockManager::perspectiveOpened(const QString & _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 5, _a);
}

// SIGNAL 6
void ads::CDockManager::floatingWidgetCreated(CFloatingDockContainer * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 6, _a);
}

// SIGNAL 7
void ads::CDockManager::dockAreaCreated(CDockAreaWidget * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 7, _a);
}

// SIGNAL 8
void ads::CDockManager::dockWidgetAboutToBeRemoved(CDockWidget * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 8, _a);
}

// SIGNAL 9
void ads::CDockManager::dockWidgetRemoved(CDockWidget * _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(std::addressof(_t1))) };
    QMetaObject::activate(this, &staticMetaObject, 9, _a);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
