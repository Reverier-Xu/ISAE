cmake_minimum_required(VERSION 3.5)
find_package(Qt5 5.15 COMPONENTS Core Gui Widgets REQUIRED)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

project(ISAESettings LANGUAGES CXX)

set(Settings_SRCS
    settings.h
    settings.cpp
)

add_library(settings STATIC ${Settings_SRCS})

target_link_libraries(settings PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)
