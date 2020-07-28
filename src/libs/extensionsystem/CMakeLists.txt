cmake_minimum_required(VERSION 3.10)
find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(ExtensionSystem_SRCS
        ISAEPluginWidget.cpp ISAEPluginWidget.h)

add_library(ExtensionSystem ${ExtensionSystem_SRCS})

target_link_libraries(ExtensionSystem PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)

set_target_properties(ExtensionSystem PROPERTIES
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