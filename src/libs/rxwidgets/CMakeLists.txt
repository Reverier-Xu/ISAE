cmake_minimum_required(VERSION 3.10)
find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(RxWidgets_SRCS RxAnimatedWidget.cpp RxAnimatedWidget.h menubutton.cpp menubutton.h)

add_library(RxWidgets ${RxWidgets_SRCS})

target_link_libraries(RxWidgets PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)

set_target_properties(RxWidgets PROPERTIES
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
