cmake_minimum_required(VERSION 3.10)
project(editor LANGUAGES CXX)

find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)
find_package(KF5TextEditor)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(Editor_SRCS
        editor.cpp
        editor.h
        chunks.cpp
        chunks.h
        hexeditor.cpp
        hexeditor.h
        commands.cpp
        commands.h
        editorSettingPage.cpp
        editorSettingPage.h)

qt5_add_resources(RESOURCES "${CMAKE_CURRENT_SOURCE_DIR}/../../resources/app.qrc")
add_library(Editor STATIC ${Editor_SRCS})

target_link_libraries(Editor PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets KF5::TextEditor)
target_link_libraries(Editor PRIVATE ExtensionSystem RxWidgets isaeutils)

target_include_directories(Editor PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/extensionsystem"
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/rxwidgets"
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/utils")

set_target_properties(Editor PROPERTIES
        AUTOMOC ON
        AUTORCC ON
        AUTOUIC ON
        CXX_STANDARD 17
        CXX_STANDARD_REQUIRED ON
        CXX_EXTENSIONS OFF
        ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
