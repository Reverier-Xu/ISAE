cmake_minimum_required(VERSION 3.10)
project(filemanager LANGUAGES CXX)

find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(FileManager_SRCS
        filemanager.cpp
        filemanager.h
        filemanager.ui
        filemanagerSettingPage.cpp
        filemanagerSettingPage.h
        filemanagerSettingPage.ui)

qt5_add_resources(RESOURCES "${CMAKE_CURRENT_SOURCE_DIR}/../../resources/app.qrc")
add_library(FileManager STATIC ${FileManager_SRCS})

target_link_libraries(FileManager PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)
target_link_libraries(FileManager PRIVATE ExtensionSystem RxWidgets isaeutils)

target_include_directories(FileManager PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/extensionsystem"
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/rxwidgets"
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/utils")

set_target_properties(FileManager PROPERTIES
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
