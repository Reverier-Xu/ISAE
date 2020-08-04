cmake_minimum_required(VERSION 3.10)
project(console LANGUAGES CXX)

find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(Console_SRCS console.cpp console.h)

qt5_add_resources(RESOURCES "${CMAKE_CURRENT_SOURCE_DIR}/../../resources/app.qrc")
add_library(Console STATIC ${Console_SRCS})

    target_link_libraries(Console PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)
target_link_libraries(Console PRIVATE ExtensionSystem RxWidgets isaeutils qtermwidget5)

target_include_directories(Console PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/extensionsystem"
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/rxwidgets"
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/utils"
        "${CMAKE_CURRENT_SOURCE_DIR}/../../libs/qterm")

set_target_properties(Console PROPERTIES
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