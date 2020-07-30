cmake_minimum_required(VERSION 3.10)
find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(MainApp_SRCS
        main.cpp
        MainApp.cpp
        MainApp.h
        MainApp.ui
        MainAppSettingPage.cpp
        MainAppSettingPage.h
        MainAppSettingPage.ui
        SettingWindow.cpp
        SettingWindow.h
        SettingWindow.ui
        AboutWindow.cpp
        AboutWindow.h
        AboutWindow.ui
        DonateWindow.cpp
        DonateWindow.h
        DonateWindow.ui)
qt5_add_resources(RESOURCES "${CMAKE_CURRENT_SOURCE_DIR}/../resources/app.qrc")

add_executable(MainApp ${MainApp_SRCS} ${RESOURCES})

target_link_libraries(MainApp PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)
target_link_libraries(MainApp PRIVATE
        qtadvanceddocking
        nodes
        ExtensionSystem
        RxWidgets
        isaeutils
        FileManager
        Editor
        )

target_include_directories(MainApp PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/../libs/advanceddockingsystem"
        "${CMAKE_CURRENT_SOURCE_DIR}/../libs/nodeeditor"
        "${CMAKE_CURRENT_SOURCE_DIR}/../libs/extensionsystem"
        "${CMAKE_CURRENT_SOURCE_DIR}/../libs/rxwidgets"
        "${CMAKE_CURRENT_SOURCE_DIR}/../libs/utils"
        "${CMAKE_CURRENT_SOURCE_DIR}/../extensions/filemanager"
        "${CMAKE_CURRENT_SOURCE_DIR}/../extensions/editor")

set_target_properties(MainApp PROPERTIES
        AUTOMOC ON
        AUTORCC ON
        AUTOUIC ON
        CXX_STANDARD 17
        CXX_STANDARD_REQUIRED ON
        CXX_EXTENSIONS OFF
        ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
        )
