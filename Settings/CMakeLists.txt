cmake_minimum_required(VERSION 3.5)
find_package(Qt5 5.15 COMPONENTS Core Gui Widgets REQUIRED)
set(CMAKE_INCLUDE_CURRENT_DIR ON)


set(Settings_SRCS
    settings.cpp
    settings.h
)

add_library(settings STATIC ${Settings_SRCS})

target_link_libraries(settings PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)
