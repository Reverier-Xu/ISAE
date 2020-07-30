cmake_minimum_required(VERSION 3.10)
find_package(Qt5 5.5 COMPONENTS Core Gui Widgets REQUIRED)
set(CMAKE_INCLUDE_CURRENT_DIR ON)


set(ISAEUtils_SRCS
        isaeutils.cpp
        isaeutils.h)

add_library(isaeutils STATIC ${ISAEUtils_SRCS})

set_target_properties(isaeutils PROPERTIES
        AUTOMOC ON
        AUTORCC ON
        AUTOUIC ON
        CXX_STANDARD 17
        CXX_STANDARD_REQUIRED ON
        CXX_EXTENSIONS ON
        ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
        )

target_link_libraries(isaeutils PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)
