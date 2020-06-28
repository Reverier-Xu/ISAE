cmake_minimum_required(VERSION 3.5)
find_package(Qt5 5.5 COMPONENTS Core Gui Widgets REQUIRED)
set(CMAKE_INCLUDE_CURRENT_DIR ON)


set(ISAEUtils_SRCS
    isaeutils.cpp
    isaeutils.h
)

add_library(isaeutils STATIC ${ISAEUtils_SRCS})

target_link_libraries(isaeutils PUBLIC Qt5::Core Qt5::Gui Qt5::Widgets)
